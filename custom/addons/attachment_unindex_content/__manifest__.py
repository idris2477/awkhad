# © 2019  Vauxoo (<http://www.vauxoo.com/>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Attachment Unindex Content',
    'summary': 'Disable indexing of attachments',
    'version': '12.0.1.0.0',
    'author': 'Vauxoo, Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/server-tools',
    'maintainers': ['moylop260', 'ebirbe'],
    'license': 'AGPL-3',
    'category': 'Tools',
    'depends': [
        'base',
    ],
    'installable': True,
    'application': False,
    'post_init_hook': 'post_init_hook',
}
