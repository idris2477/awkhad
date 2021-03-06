# Copyright 2019 Eugene Molotov <https://github.com/em230418>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import awkhad.tests
from ..models.ir_translation import debrand_bytes


@awkhad.tests.common.tagged('at_install', 'post_install')
class TestMisc(awkhad.tests.TransactionCase):

    def test_debrand_bytes(self):
        env = self.env
        env['ir.config_parameter'].sudo().set_param("web_debranding.new_name", "SuperName")
        assert debrand_bytes(env, b'awkhad') == b'SuperName'
        assert debrand_bytes(env, 'awkhad') == b'SuperName'
        assert debrand_bytes(env, b'test') == b'test'
        assert debrand_bytes(env, 'test') == b'test'
