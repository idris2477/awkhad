# Copyright 2017 Angel Moya (PESOL)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from awkhad.tests.common import TransactionCase
from awkhad import fields


class ManifestWizardCase(TransactionCase):
    def setUp(self):
        super(ManifestWizardCase, self).setUp()
        self.free_delivery = self.env.ref('delivery.free_delivery_carrier')

    def test_wizard(self):
        """Create manifest wizard.
        """
        wizard = self.env['manifest.wizard'].create({
            'carrier_id': self.free_delivery.id,
            'from_date': fields.Date.today()
        })
        with self.assertRaises(NotImplementedError):
            wizard.get_manifest_file()