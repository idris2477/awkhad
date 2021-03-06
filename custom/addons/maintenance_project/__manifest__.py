# Copyright 2019 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    'name': 'Maintenance Projects',
    "summary": "Adds projects to maintenance equipments and requests",
    "version": "12.0.1.0.0",
    "author": "Awkhad Community Association (ACA), Solvos",
    'license': 'AGPL-3',
    "category": "Maintenance",
    "website": "https://github.com/ACA/maintenance",
    "depends": [
        "maintenance",
        "project",
    ],
    "data": [
        "security/maintenance_project_security.xml",
        "views/maintenance_equipment_views.xml",
        "views/maintenance_request_views.xml",
        "views/project_project_views.xml",
    ],
    "demo": [
        "data/demo_maintenance_project.xml",
    ],
    'installable': True,
}
