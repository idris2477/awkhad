# -*- coding: utf-8 -*-
# Part of Awkhad. See LICENSE file for full copyright and licensing details.

from awkhad import api, exceptions, fields, models, _


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    use_next_on_work_order_id = fields.Many2one('mrp.workorder',
        string="Next Work Order to Use",
        help='Technical: used to figure out default serial number on work orders')
