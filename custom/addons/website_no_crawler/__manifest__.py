# Copyright 2016 B-informed B.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Alter robots.txt disallow indexing',
    'summary': 'Disables robots.txt for indexing by webcrawlers like Google',
    'license': 'AGPL-3',
    'version': '12.0.1.1.0',
    'website': 'https://github.com/ACA/website',
    'author': "B-Informed B.V.,Awkhad Community Association (ACA)",
    'category': 'Website',
    'depends': [
        'website',
    ],
    'data': [
        'views/disable_robots.xml',
    ],
    'installable': True,
}