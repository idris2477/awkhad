# Copyright 2016-2019 Akretion France (https://akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Purchase Commercial Partner',
    'version': '12.0.1.0.0',
    'category': 'Purchases',
    'license': 'AGPL-3',
    'summary': "Add stored related field 'Commercial Supplier' on POs",
    'author': 'Akretion,Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/purchase-workflow',
    'depends': ['purchase'],
    'data': [
        'views/purchase.xml',
    ],
    'installable': True,
}