# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account - Chart of Accounts Menus',
    'version': '12.0.1.0.0',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'summary': "Adds menu entries for Chart of Accounts templates",
    'author': "GRAP, Awkhad Community Association (ACA)",
    'website': 'https://github.com/ACA/account-financial-tools',
    'depends': [
        'account',
    ],
    'data': [
        'views/menu.xml',
        'views/account_chart_template.xml',
        'views/account_account_template.xml',
        'views/account_tax_template.xml',
        'views/account_fiscal_position_template.xml',

    ],
    'installable': True,
}
