# Copyright 2017 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# Copyright 2017-2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import awkhad.tests


@awkhad.tests.common.tagged('post_install', 'at_install')
class TestUi(awkhad.tests.HttpCase):

    # big timeout due to long redirects (checkout -> confirmation) in nobill cases
    def test_checkout_nobill_noship(self):
        self.browser_js("/",
                        "awkhad.__DEBUG__.services['web_tour.tour'].run('shop_mandatory_fields_nobill_noship', 10000)",
                        "awkhad.__DEBUG__.services['web_tour.tour'].tours.shop_mandatory_fields_nobill_noship.ready",
                        login=None, timeout=160)

    def test_checkout_bill_noship(self):
        self.browser_js("/",
                        "awkhad.__DEBUG__.services['web_tour.tour'].run('shop_mandatory_fields_bill_noship', 3000)",
                        "awkhad.__DEBUG__.services['web_tour.tour'].tours.shop_mandatory_fields_bill_noship.ready",
                        login=None, timeout=170)

    def test_checkout_bill_ship(self):
        self.browser_js("/",
                        "awkhad.__DEBUG__.services['web_tour.tour'].run('shop_mandatory_fields_bill_ship', 3000)",
                        "awkhad.__DEBUG__.services['web_tour.tour'].tours.shop_mandatory_fields_bill_ship.ready",
                        login=None, timeout=200)

    def test_checkout_nobill_ship(self):
        self.browser_js("/",
                        "awkhad.__DEBUG__.services['web_tour.tour'].run('shop_mandatory_fields_nobill_ship', 10000)",
                        "awkhad.__DEBUG__.services['web_tour.tour'].tours.shop_mandatory_fields_nobill_ship.ready",
                        login=None, timeout=190)
