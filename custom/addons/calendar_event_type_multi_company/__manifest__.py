# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Calendar Event Type Multi Company',
    'summary': """
        This module add multi-company management to calendar event type""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV,'
              'Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/multi-company',
    'depends': ['calendar'],
    'data': [
        'security/calendar_event_type.xml',
        'views/calendar_event_type.xml',
    ],
}
