# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import fields, models


class FSMTemplate(models.Model):
    _inherit = 'fsm.template'

    skill_ids = fields.Many2many('hr.skill', string="Required Skills")
