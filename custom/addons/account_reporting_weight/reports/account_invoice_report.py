# Copyright 2017 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import fields, models
import awkhad.addons.decimal_precision as dp


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    weight = fields.Float(digits=dp.get_precision('Stock Weight'))

    def _select(self):
        select_str = super()._select()
        select_str += """
            , sub.weight as weight
            """
        return select_str

    def _sub_select(self):
        select_str = super()._sub_select()
        select_str += """
            , SUM(pr.weight * ail.quantity / u.factor * u2.factor)
            AS weight
            """
        return select_str

    def _group_by(self):
        group_by_str = super()._group_by()
        group_by_str += ", pr.weight, u.category_id"
        return group_by_str
