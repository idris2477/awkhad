# Copyright 2013 Camptocamp SA (http://www.camptocamp.com)
# @author Nicolas Bessi
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{'name': 'Accounting Payment Access',
 'summary': 'Prevent the usage of payments from invoices',
 'version': '12.0.1.0.0',
 'category': 'other',
 'author': 'Camptocamp,Awkhad Community Association (ACA)',
 'website': 'https://github.com/ACA/account-payment',
 'license': 'AGPL-3',
 'depends': ['account'],
 'data': [
     'security/invoice_data.xml',
     'view/invoice_view.xml'
 ],
 'installable': True,
 }
