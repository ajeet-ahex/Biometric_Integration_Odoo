from odoo import models, fields, api
from zk import ZK
from datetime import datetime
from pytz import timezone,utc
import pytz


class BiometricAttendance(models.Model):
    _name = 'biometric.attendance'
    _description = 'Biometric Attendance'

    user_id = fields.Char(string="User ID")
    name = fields.Char(string="Name")
    timestamp = fields.Datetime(string="Timestamp Essl")
    formatted_datetime = fields.Char(string="Timestamp", compute='_compute_formatted_datetime')

    @api.depends('timestamp')
    def _compute_formatted_datetime(self):
        for record in self:
            if record.timestamp:
                record.formatted_datetime = fields.Datetime.to_string(record.timestamp)
            else:
                record.formatted_datetime = ''