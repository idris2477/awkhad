# Copyright 2014 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from awkhad import api
from awkhad import models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.multi
    def write(self, vals):
        res = super(HrEmployee, self).write(vals)
        for r in self:
            r.user_id.render_signature_id()
        return res
