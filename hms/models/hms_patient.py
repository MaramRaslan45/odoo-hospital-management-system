import re
from datetime import date

from odoo import models,fields,api
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hms.patient'
    _rec_name = 'firstname'

    firstname = fields.Char()
    lastname = fields.Char()
    birthdate = fields.Date()
    history = fields.Html()
    CR_Ratio = fields.Float()
    Blood_Type = fields.Selection([
        ('b', 'B'),
        ('a', 'A'),
        ('o','O')
    ])
    PCR = fields.Boolean()
    image = fields.Image()
    Address = fields.Text()
    email = fields.Text()
    Age = fields.Integer()
    department_id = fields.Many2one('hms.department')
    doctors_ids = fields.Many2many('hms.doctors')
    Capacity = fields.Integer(related='department_id.Capacity')
    history_ids = fields.One2many('patient.history','patient_id')
    # partner_id = fields.Many2one('res.partner')
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], default='undetermined')

    def next_stage(self):
        if self.state == 'undetermined':
            self.state = 'good'
        elif self.state == 'good':
            self.state = 'fair'
        elif self.state == 'fair':
            self.state = 'serious'
        p_history = self.env['patient.history'].create({
            'created_by': self.doctors_ids.firstname,
            'date': date.today(),
            'description': f'state changed to {self.state}',

        })

    _sql_constraints = [
        # ('constraint name', 'constraint type', 'message ')
        ('unique_email', 'UNIQUE(email)', 'This Email already exists'),
    ]

    @api.onchange('Age')
    def _onchange_age(self):
        if self.Age < 30 and self.Age > 0:
            self.PCR = True

            return {
                'warning': {'title': 'Warning!', 'message': 'PCR is checked'},
            }


    @api.constrains('email')
    def _validate_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if self.email:
            if not re.fullmatch(regex,self.email):
                raise ValidationError('Enter valid email address')

    @api.onchange('birthdate')
    def _onchange_birth_date(self):
        if self.birthdate:
            self.Age = date.today().year - self.birthdate.year


