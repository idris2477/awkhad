# Copyright 2018 - Today Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Point of Sale - Picking Creation Delayed',
    'summary': 'Delay the creation of the picking when PoS order is created',
    'version': '12.0.1.0.0',
    'category': 'Point Of Sale',
    'author': 'GRAP, '
              'Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'website': 'https://www.github.com/ACA/pos',
    'depends': [
        'point_of_sale',
        'queue_job',
    ],
    'data': [
        'views/view_pos_config.xml',
        'views/view_pos_order.xml',
    ],
    'images': [
        'static/description/pos_order_tree.png',
    ],
    'installable': True,
}
