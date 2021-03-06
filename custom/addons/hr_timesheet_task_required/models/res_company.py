# Copyright 2018-2019 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from awkhad import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    is_timesheet_task_required = fields.Boolean(
        string='Require Tasks on Timesheets',
    )
