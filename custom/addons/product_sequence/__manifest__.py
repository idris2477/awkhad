# Copyright 2004 Tiny SPRL
# Copyright 2016 Sodexis
# Copyright 2018 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Product Sequence',
    'version': '12.0.1.0.1',
    'author': "Zikzakmedia SL,Sodexis,Awkhad Community Association (ACA)",
    'website': 'https://github.com/ACA/product-attribute',
    'license': 'AGPL-3',
    'category': 'Product',
    'depends': [
        'product',
        'product_code_unique',
    ],
    'data': [
        'data/product_sequence.xml',
        'views/product_category.xml',
    ],
    'pre_init_hook': 'pre_init_hook',
    'installable': True,
}
