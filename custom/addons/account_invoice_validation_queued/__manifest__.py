# Copyright 2019 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Enqueue account invoice validation',
    'version': '12.0.1.0.0',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'author': 'Tecnativa, '
              'Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/account-invoicing',
    'depends': [
        'account',
        'queue_job',
    ],
    'data': [
        'views/queue_job_views.xml',
        'views/account_invoice_views.xml',
        'wizards/account_invoice_confirm_views.xml',
    ],
    'installable': True,
    'development_status': 'Production/Stable',
    'maintainers': ['pedrobaeza'],
}
