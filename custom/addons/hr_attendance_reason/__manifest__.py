# Copyright 2017 Awkhad S.A.
# Copyright 2018 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

{
    'name': 'HR Attendance Reason',
    'version': '12.0.1.0.0',
    'category': 'Human Resources',
    'website': 'https://github.com/ACA/hr',
    'author': 'Awkhad S.A.,'
              'Awkhad Community Association (ACA)',
    'license': 'LGPL-3',
    'installable': True,
    'depends': [
        'hr_attendance',
    ],
    'data': [
        'data/hr_attendance_reason_data.xml',
        'security/ir.model.access.csv',
        'views/hr_attendance_reason_view.xml',
        'views/hr_attendance_view.xml',
    ],
}
