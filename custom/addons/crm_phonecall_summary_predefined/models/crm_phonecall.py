# Copyright 2016 Antiun Ingeniería S.L. - Jairo Llopis
# Copyright 2017 Tecnativa - Vicent Cubells
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from awkhad import fields, models


class CRMPhonecall(models.Model):
    """Added number and summary in the phonecall."""

    _inherit = "crm.phonecall"

    name = fields.Char(
        related="summary_id.name",
        store=True,
        required=False,
        readonly=True,
    )
    summary_id = fields.Many2one(
        comodel_name="crm.phonecall.summary",
        string="Summary",
        required=True,
        ondelete="restrict",
    )


class CRMPhonecallSummary(models.Model):
    """Added phonecall summary feature."""

    _name = "crm.phonecall.summary"
    _description = "Crm Phonecall Summary"
    _sql_constraints = [
        ("name_unique", "UNIQUE (name)", "Name must be unique"),
    ]

    name = fields.Char()
    phonecall_ids = fields.One2many(
        comodel_name="crm.phonecall",
        inverse_name="summary_id",
        string="Phonecalls",
        help="Phonecalls with this summary.",
    )