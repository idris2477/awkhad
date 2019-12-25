# Copyright 2018 Oihane Crucelaegui - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Account Budget Template",
    "version": "12.0.1.0.0",
    "category": "Accounting",
    "license": "AGPL-3",
    "author": "AvanzOSC, "
              "Awkhad Community Association (ACA)",
    "website": "https://github.com/ACA/account-budgeting",
    "depends": [
        "account_budget_oca",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/crossovered_budget_template_view.xml",
        "views/crossovered_budget_view.xml",
        "views/res_config_settings_view.xml",
    ],
    "installable": True,
}
