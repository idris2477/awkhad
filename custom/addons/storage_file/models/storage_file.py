# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import base64
import hashlib
import logging
import mimetypes
import os
import re

from awkhad import api, fields, models
from awkhad.exceptions import UserError
from awkhad.tools import human_size
from awkhad.tools.translate import _

_logger = logging.getLogger(__name__)

try:
    from slugify import slugify
except ImportError:  # pragma: no cover
    _logger.debug("Cannot `import slugify`.")


REGEX_SLUGIFY = r"[^-a-z0-9_]+"


class StorageFile(models.Model):
    _name = "storage.file"
    _description = "Storage File"

    name = fields.Char(required=True, index=True)
    backend_id = fields.Many2one(
        "storage.backend", "Storage", index=True, required=True
    )
    url = fields.Char(compute="_compute_url", help="HTTP accessible path to the file")
    relative_path = fields.Char(readonly=True, help="Relative location for backend")
    file_size = fields.Integer("File Size")
    human_file_size = fields.Char(
        "Human File Size", compute="_compute_human_file_size", store=True
    )
    checksum = fields.Char("Checksum/SHA1", size=40, index=True, readonly=True)
    filename = fields.Char(
        "Filename without extension", compute="_compute_extract_filename", store=True
    )
    extension = fields.Char(
        "Extension", compute="_compute_extract_filename", store=True
    )
    mimetype = fields.Char("Mime Type", compute="_compute_extract_filename", store=True)
    data = fields.Binary(
        help="Datas", inverse="_inverse_data", compute="_compute_data", store=False
    )
    to_delete = fields.Boolean()
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        "res.company", "Company", default=lambda self: self.env.user.company_id.id
    )
    file_type = fields.Selection([])

    _sql_constraints = [
        (
            "path_uniq",
            "unique(relative_path, backend_id)",
            "The private path must be uniq per backend",
        )
    ]

    def write(self, vals):
        if "data" in vals:
            for record in self:
                if record.data:
                    raise UserError(
                        _("File can not be updated," "remove it and create a new one")
                    )
        return super(StorageFile, self).write(vals)

    @api.depends("file_size")
    def _compute_human_file_size(self):
        for record in self:
            record.human_file_size = human_size(self.file_size)

    def _slugify_name_with_id(self):
        return u"{}{}".format(
            slugify(
                u"{}-{}".format(self.filename, self.id), regex_pattern=REGEX_SLUGIFY
            ),
            self.extension,
        )

    def _build_relative_path(self, checksum):
        self.ensure_one()
        strategy = self.sudo().backend_id.filename_strategy
        if not strategy:
            raise UserError(
                _(
                    "The filename strategy is empty for the backend %s.\n"
                    "Please configure it"
                )
                % self.backend_id.name
            )
        if strategy == "hash":
            return checksum[:2] + "/" + checksum
        elif strategy == "name_with_id":
            return self._slugify_name_with_id()

    def _prepare_meta_for_file(self):
        bin_data = base64.b64decode(self.data)
        checksum = hashlib.sha1(bin_data).hexdigest()
        relative_path = self._build_relative_path(checksum)
        return {
            "checksum": checksum,
            "file_size": len(bin_data),
            "relative_path": relative_path,
        }

    def _inverse_data(self):
        for record in self:
            record.write(record._prepare_meta_for_file())
            record.backend_id.sudo()._add_b64_data(
                record.relative_path, record.data, mimetype=record.mimetype
            )

    def _compute_data(self):
        for rec in self:
            if self._context.get("bin_size"):
                rec.data = rec.file_size
            elif rec.relative_path:
                rec.data = rec.backend_id.sudo()._get_b64_data(rec.relative_path)
            else:
                rec.data = None

    @api.depends(
        "backend_id.served_by",
        "backend_id.base_url",
        "backend_id.url_include_directory_path",
        "relative_path",
    )
    def _compute_url(self):
        for record in self:
            record.url = record._get_url()

    def _get_url(self):
        """Retrieve file URL based on backend params."""
        backend = self.backend_id.sudo()
        parts = []
        if backend.served_by == "awkhad":
            params = self.env["ir.config_parameter"].sudo()
            parts = [
                params.get_param("web.base.url"),
                "storage.file",
                self._slugify_name_with_id(),
            ]
        else:
            parts = [backend.base_url or ""]
            if backend.url_include_directory_path and backend.directory_path:
                parts.append(backend.directory_path)
            parts.append(self.relative_path)
        return "/".join(parts)

    @api.depends("name")
    def _compute_extract_filename(self):
        for rec in self:
            rec.filename, rec.extension = os.path.splitext(rec.name)
            mime, __ = mimetypes.guess_type(rec.name)
            rec.mimetype = mime

    def unlink(self):
        if self._context.get("cleanning_storage_file"):
            super(StorageFile, self).unlink()
        else:
            self.write({"to_delete": True, "active": False})
        return True

    @api.model
    def _clean_storage_file(self):
        self._cr.execute(
            """SELECT id
            FROM storage_file
            WHERE to_delete=True FOR UPDATE"""
        )
        ids = [x[0] for x in self._cr.fetchall()]
        for st_file in self.browse(ids):
            st_file.backend_id.sudo()._delete(st_file.relative_path)
            st_file.with_context(cleanning_storage_file=True).unlink()
            st_file._cr.commit()

    @api.model
    def get_from_slug_name_with_id(self, slug_name_with_id):
        """
        Return a browse record from a string generated by the method
        _slugify_name_with_id
        :param slug_name_with_id:
        :return: a BrowseRecord (could be empty...)
        """
        # id is the last group of digit after '-'
        _id = re.findall(r"-([0-9]+)", slug_name_with_id)[-1:]
        if _id:
            _id = int(_id[0])
        return self.browse(_id)
