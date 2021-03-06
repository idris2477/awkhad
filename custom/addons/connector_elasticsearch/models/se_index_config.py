# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import json

from awkhad import api, fields, models


class SeIndexConfig(models.Model):

    _name = "se.index.config"
    _description = "Elasticsearch index configuration"

    name = fields.Char(required=True)
    body = fields.Serialized(required=True)
    # This field is used since no widget exists to edit a serialized field
    # into the web fontend
    body_str = fields.Text(compute="_compute_body_str", inverse="_inverse_body_str")

    @api.multi
    @api.depends("body")
    def _compute_body_str(self):
        for rec in self:
            if rec.body:
                rec.body_str = json.dumps(rec.body)

    @api.multi
    def _inverse_body_str(self):
        for rec in self:
            data = None
            if rec.body_str:
                data = json.loads(rec.body_str)
            rec.body = data
