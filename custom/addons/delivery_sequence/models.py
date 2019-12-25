from zgui import fields
from zgui import models


class DeliveryCarrier(models.Model):
    _inherit = "delivery.carrier"

    _order = 'sequence,id'

    sequence = fields.Integer('Sequence', default=0)
