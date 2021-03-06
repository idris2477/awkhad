# -*- coding: utf-8 -*-
# Copyright 2018 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from awkhad import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    media_ids = fields.Many2many("storage.media")
