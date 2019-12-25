# Copyright 2019 Artem Rafailov <https://it-projects.info/team/Ommo73/>
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl.html).

import awkhad.tests
from awkhad.api import Environment


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_pos_scan_ref(self):
        cr = self.registry.cursor()
        env = Environment(cr, self.uid, {})
        env['ir.module.module'].search([('name', '=', 'pos_scan_ref')], limit=1).state = 'installed'
        env['product.template'].search([('name', '=', "Boni Oranges")], limit=1).write({
            'default_code': '1234567890333',
        })
        cr.release()
        # without a delay there might be problems on the steps whilst opening a POS
        # caused by a not yet loaded button's action
        self.phantom_js("/web",
                        "awkhad.__DEBUG__.services['web_tour.tour'].run('tour_pos_scan_ref', 1000)",
                        "awkhad.__DEBUG__.services['web_tour.tour'].tours.tour_pos_scan_ref.ready",
                        login="admin", timeout=140)
