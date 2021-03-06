# Copyright 2019 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from awkhad import models


class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom,
                               location_id, name, origin, values, group_id):
        res = super(StockRule, self)._get_stock_move_values(
            product_id, product_qty, product_uom, location_id, name, origin,
            values, group_id
        )
        if values.get('sale_line_id', False):
            sale_line = self.env['sale.order.line'].browse(
                values['sale_line_id'])
            if sale_line.secondary_uom_id:
                res.update({
                    'secondary_uom_id': sale_line.secondary_uom_id.id,
                    'secondary_uom_qty': sale_line.secondary_uom_qty,
                })
        return res
