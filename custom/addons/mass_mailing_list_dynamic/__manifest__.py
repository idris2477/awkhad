# Copyright 2017 Tecnativa - Jairo Llopis
# Copyright 2018 Tecnativa - David Vidal
# Copyright 2019 Tecnativa - Victor Martin
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Dynamic Mass Mailing Lists",
    "summary": "Mass mailing lists that get autopopulated",
    "version": "12.0.1.0.0",
    "category": "Marketing",
    "website": "https://github.com/ACA/social",
    "author": "Tecnativa, Awkhad Community Association (ACA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "mass_mailing_partner",
    ],
    "data": [
        # This should go first
        "wizards/mail_mass_mailing_load_filter_views.xml",
        "views/mail_mass_mailing_list_view.xml",
    ],
}
