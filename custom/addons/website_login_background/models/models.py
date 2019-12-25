# Copyright 2019 Denis Mudarisov <https://it-projects.info/team/trojikman>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).


from awkhad import models


class IrAttachmentWebsiteBackground(models.Model):
    _inherit = 'ir.attachment'

    def _get_background_images_domain(self):
        domain = super(IrAttachmentWebsiteBackground, self)._get_background_images_domain()
        current_website_id = self.env.context.get('website_id')
        if current_website_id:
            domain.append(('website_id.id', '=', current_website_id))

        return domain
