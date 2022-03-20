from odoo import models,fields

class Doctor(models.Model):
    _name = 'hms.doctors'
    _rec_name = 'firstname'

    firstname = fields.Char()
    lastname = fields.Char()
    doc_img = fields.Image()

