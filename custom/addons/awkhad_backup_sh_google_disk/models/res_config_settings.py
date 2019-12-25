# Copyright 2019 Dinar Gabbasov <https://it-projects.info/team/GabbasovDinar>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from awkhad import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    google_service_account_key = fields.Char(string="Service Account Key",
                                             help="Credentials in json format")
    google_disk_folder_id = fields.Char(string="Google Drive Folder ID")

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        ICPSudo.set_param("awkhad_backup_sh_google_disk.service_account_key", self.google_service_account_key or '')
        ICPSudo.set_param("awkhad_backup_sh_google_disk.google_disk_folder_id", self.google_disk_folder_id or '')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        google_service_account_key = ICPSudo.get_param("awkhad_backup_sh_google_disk.service_account_key")
        google_disk_folder_id = ICPSudo.get_param("awkhad_backup_sh_google_disk.google_disk_folder_id")
        res.update(
            google_service_account_key=google_service_account_key or False,
            google_disk_folder_id=google_disk_folder_id or False,
        )
        return res
