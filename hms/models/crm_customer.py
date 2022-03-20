from odoo import models,fields,api
from odoo.exceptions import UserError


class Customer(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient')

    @api.constrains('related_patient_id')
    def _check_mail(self):
        if self.email == self.related_patient_id.Email:
            raise UserError("This email already exists")

    def unlink(self):
        if self.related_patient_id:
            raise UserError("Cant delete accepted student")
        super().unlink()


