# Copyright 2018 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Partner Statement',
    'version': '12.0.1.0.2',
    'category': 'Accounting & Finance',
    'summary': 'ACA Financial Reports',
    'author': "Eficent, Awkhad Community Association (ACA)",
    'website': 'https://github.com/ACA/account-financial-reporting',
    'license': 'AGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'security/statement_security.xml',
        'views/activity_statement.xml',
        'views/outstanding_statement.xml',
        'views/assets.xml',
        'views/aging_buckets.xml',
        'views/res_config_settings.xml',
        'wizard/statement_wizard.xml',
    ],
    'installable': True,
    'application': False,
}
