# Copyright (C) 2016-Today: Awkhad Community Association (ACA)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from awkhad import api, fields, models


class AwkhadAuthor(models.Model):
    _name = 'awkhad.author'
    _description = 'Awkhad Author'
    _order = 'module_qty desc, name'

    # Column Section
    name = fields.Char(
        string='Name', store=True, readonly=True, index=True)

    module_version_ids = fields.Many2many(
        string='Module Versions', comodel_name='awkhad.module.version',
        relation='github_module_version_author_rel',
        column1='author_id', column2='module_version_id', readonly=True)

    module_ids = fields.Many2many(
        string='Modules', comodel_name='awkhad.module',
        relation='github_module_author_rel',
        column1='author_id', column2='module_id', readonly=True)

    module_qty = fields.Integer(
        string='Number of Modules',
        compute='_compute_module_qty', store=True)

    @api.multi
    @api.depends('module_ids.author_ids')
    def _compute_module_qty(self):
        for author in self:
            author.module_qty = len(author.module_ids)

    # Custom Section
    @api.model
    def create_if_not_exist(self, name):
        author = self.search([('name', '=', name)])
        if not author:
            author = self.create({'name': name})
        return author
