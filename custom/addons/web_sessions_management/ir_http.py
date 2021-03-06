import random
import zgui
from zgui import api
from zgui import models
from zgui.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def _auth_method_user(self):
        super(IrHttp, self)._auth_method_user()
        if random.random() < 0.01:
            with zgui.registry(request.cr.dbname).cursor() as cr:
                cr.autocommit(True)
                env = api.Environment(cr, request.uid, request.context)
                env['ir.sessions'].update_last_activity(request.session.sid)
                cr.commit()
