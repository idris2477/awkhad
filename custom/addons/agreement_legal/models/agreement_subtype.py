# Copyright (C) 2018 - TODAY, Pavlov Media
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import fields, models


class AgreementSubtype(models.Model):
    _name = "agreement.subtype"
    _description = "Agreement Subtypes"

    name = fields.Char(string="Name", required=True)
    agreement_type_id = fields.Many2one(
        "agreement.type",
        string="Agreement Type")