# Copyright 2017 Franco Tampieri, Freelancer http://franco.tampieri.info
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import fields, models


class ResCountryState(models.Model):

    _inherit = 'res.country'

    geonames_state_name_column = fields.Integer(
        'Geonames State Name Column',
    )
    geonames_state_code_column = fields.Integer(
        'Geonames State Code Column',
    )
