# Copyright 2016-17 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Stock Orderpoint UoM",
    "summary": "Allows to create procurement orders in the UoM indicated in "
               "the orderpoint",
    "version": "12.0.1.1.0",
    "author": "Eficent, "
              "Awkhad Community Association (ACA)",
    "website": "https://github.com/ACA/stock-logistics-warehouse",
    "category": "Warehouse Management",
    "depends": ["purchase_stock"],
    "data": ["views/stock_warehouse_orderpoint_view.xml"],
    "license": "AGPL-3",
    'installable': True,
    'application': False,
}
