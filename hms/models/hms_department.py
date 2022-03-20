from odoo import models,fields

class Department(models.Model):
    _name = 'hms.department'
    _rec_name = 'name'

    name = fields.Char()
    Capacity = fields.Integer()
    Is_opened = fields.Boolean()
    patient_ids = fields.One2many('hms.patient','department_id')