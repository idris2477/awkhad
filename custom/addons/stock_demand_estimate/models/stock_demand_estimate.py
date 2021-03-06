# Copyright 2016 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# Copyright 2016 Aleph Objects, Inc. (https://www.alephobjects.com/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from awkhad import api, fields, models, _
from awkhad.addons import decimal_precision as dp
from awkhad.exceptions import UserError


class StockDemandEstimate(models.Model):
    _name = 'stock.demand.estimate'
    _description = 'Stock Demand Estimate Line'

    date_range_id = fields.Many2one(
        comodel_name="date.range",
        string="Estimating Period",
        required=True,
        ondelete='restrict'
    )
    product_id = fields.Many2one(
        comodel_name="product.product",
        string="Product",
        required=True,
    )
    product_uom = fields.Many2one(
        comodel_name="uom.uom",
        string="Unit of measure",
    )
    location_id = fields.Many2one(
        comodel_name="stock.location",
        string="Location",
        required=True,
    )
    product_uom_qty = fields.Float(
        string="Quantity",
        digits=dp.get_precision('Product Unit of Measure'),
    )
    product_qty = fields.Float(
        'Real Quantity',
        compute='_compute_product_quantity',
        inverse='_inverse_product_quantity',
        digits=0,
        store=True,
        help='Quantity in the default UoM of the product',
    )
    daily_qty = fields.Float(
        string='Quantity / Day',
        compute='_compute_daily_qty',
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        required=True,
        default=lambda self: self.env['res.company']._company_default_get(
            'stock.demand.estimate'
        )
    )

    @api.multi
    @api.depends('product_qty', 'date_range_id.days')
    def _compute_daily_qty(self):
        for rec in self:
            if rec.date_range_id.days:
                rec.daily_qty = rec.product_qty / rec.date_range_id.days
            else:
                rec.daily_qty = 0.0

    @api.multi
    @api.depends('product_id', 'product_uom', 'product_uom_qty')
    def _compute_product_quantity(self):
        for rec in self:
            if rec.product_uom:
                rec.product_qty = rec.product_uom._compute_quantity(
                    rec.product_uom_qty, rec.product_id.uom_id
                )

    def _inverse_product_quantity(self):
        raise UserError(_(
            'The requested operation cannot be '
            'processed because of a programming error '
            'setting the `product_qty` field instead '
            'of the `product_uom_qty`.'
        ))

    @api.multi
    def name_get(self):
        res = []
        for rec in self:
            name = "%s - %s - %s" % (
                rec.date_range_id.name, rec.product_id.name,
                rec.location_id.name,
            )
            res.append((rec.id, name))
        return res

    @api.model
    def get_quantity_by_date_range(self, date_start, date_end):
        """To be used in other modules"""
        # Check if the dates overlap with the period
        period_date_start = self.date_range_id.date_start
        period_date_end = self.date_range_id.date_end

        # We need only the periods that overlap
        # the dates introduced by the user.
        if period_date_start <= date_end and period_date_end >= date_start:
            overlap_date_start = max(period_date_start, date_start)
            overlap_date_end = min(period_date_end, date_end)
            days = (abs(overlap_date_end - overlap_date_start)).days + 1
            return days * self.daily_qty
        return 0.0
