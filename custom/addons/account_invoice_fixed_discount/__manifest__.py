# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Account Fixed Discount",
    "summary": "Allows to apply fixed amount discounts in invoices.",
    "version": "12.0.1.0.1",
    "category": "Accounting & Finance",
    "website": "https://github.com/ACA/account-invoicing",
    "author": "Eficent, Awkhad Community Association (ACA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account",
    ],
    "data": [
        "views/account_invoice_view.xml",
        "reports/report_account_invoice.xml",
    ],
}
