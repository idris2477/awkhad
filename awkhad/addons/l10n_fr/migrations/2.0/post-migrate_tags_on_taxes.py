# -*- coding: utf-8 -*-
from awkhad.addons.account.models.chart_template import migrate_tags_on_taxes

def migrate(cr, version):
    migrate_tags_on_taxes(cr, None)
