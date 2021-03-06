# Copyright 2018 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Project HR',
    'summary': "Link HR with project",
    'development_status': 'Production/Stable',
    'version': '12.0.1.0.1',
    'license': 'AGPL-3',
    'author': 'Tecnativa,Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/project',
    'depends': [
        'project',
        'hr',
    ],
    'data': [
        'views/project_task_views.xml',
        'views/project_project_views.xml',
    ],
    'maintainers': [
        'pedrobaeza',
    ],
}
