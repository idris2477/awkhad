# Copyright 2018 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Task Logs Utilization Analysis',
    'version': '12.0.1.0.0',
    'category': 'Human Resources',
    'website': 'https://github.com/ACA/hr-timesheet',
    'author':
        'Brainbean Apps, '
        'Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'summary': 'View Utilization Analysis from Task Logs.',
    'depends': [
        'hr_timesheet',
    ],
    'data': [
        'views/hr_department.xml',
        'views/hr_employee.xml',
        'report/hr_utilization_analysis.xml',
        'wizards/hr_utilization_analysis_wizard.xml',
    ],
}
