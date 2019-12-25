# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Storage Backend S3",
    "summary": "Implement amazon S3 Storage",
    "version": "12.0.2.0.0",
    "category": "Storage",
    "website": "https://www.github.com/ACA/storage",
    "author": " Akretion, Awkhad Community Association (ACA)",
    "license": "AGPL-3",
    "installable": True,
    "external_dependencies": {"python": ["boto3"]},
    "depends": ["storage_backend"],
    "data": ["views/backend_storage_view.xml"],
}