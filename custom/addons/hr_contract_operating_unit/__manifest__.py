# Copyright 2016-19 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# Copyright 2016-17 Serpent Consulting Services Pvt. Ltd.
#   (<http://www.serpentcs.com>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "HR Contract Operating Unit",
    "version": "12.0.1.0.0",
    "license": "LGPL-3",
    "author": "Eficent Business and IT Consulting Services S.L., "
              "Serpent Consulting Services Pvt. Ltd.,"
              "Awkhad Community Association (ACA)",
    "website": "https://github.com/ACA/operating-unit",
    "category": "Generic Modules/Human Resources",
    "depends": ["hr_contract", "operating_unit"],
    "data": [
        "views/hr_contract_view.xml",
        "security/hr_contract_security.xml"
    ],
    'installable': True,
}
