from odoo import models, fields

class BiometricUser(models.Model):
    _name = 'biometric.user'
    _description = 'Biometric User'

    name = fields.Char(string='User Name')
    user_id = fields.Char(string='User ID')
