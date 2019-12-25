# Copyright (C) 2016-Today: Awkhad Community Association (ACA)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Github Connector - Awkhad',
    'summary': 'Analyze Awkhad modules information from Github repositories',
    'version': '12.0.1.1.0',
    'category': 'Connector',
    'license': 'AGPL-3',
    'author': 'Awkhad Community Association (ACA), Sylvain LE GAL, GRAP',
    'depends': [
        'github_connector',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/function.xml',
        'views/view_reporting.xml',
        'views/action.xml',
        'views/menu.xml',
        'views/view_awkhad_license.xml',
        'views/view_awkhad_author.xml',
        'views/view_awkhad_lib_bin.xml',
        'views/view_awkhad_lib_python.xml',
        'views/view_awkhad_module.xml',
        'views/view_awkhad_module_version.xml',
        'views/view_github_organization.xml',
        'views/view_github_repository.xml',
        'views/view_github_repository_branch.xml',
        'data/awkhad_licence.xml',
        'data/awkhad_category_data.xml',
        'data/ir_cron.xml',
    ],
    'demo': [
        'demo/github_organization.xml',
    ],
    'installable': True,
}