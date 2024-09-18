from odoo import models, api, fields
from zk import ZK
from datetime import datetime
from pytz import timezone,utc
import logging
import pytz

_logger = logging.getLogger(__name__)

class BiometricSync(models.TransientModel):
    _name = 'biometric.sync'
    _description = 'Biometric Sync'

    ip_address = fields.Char(string='IP Address', required=True, help='IP address of the biometric device')
    port = fields.Integer(string='Port', required=True, default=4370, help='Port of the biometric device')

    def sync_attendance(self):
        ip = self.ip_address
        port = self.port
        zk = ZK(ip, port=port, timeout=15)
        conn = zk.connect()

        users = conn.get_users()
        attendance_records = conn.get_attendance()
        user_dict = {user.user_id: user.name for user in users}

        _logger.info("Users dict: %s", user_dict)

        for record in attendance_records:
            user_id = record.user_id
            name = user_dict.get(user_id, 'Unknown')
            timestamp = record.timestamp

            # Get or create the biometric user in Odoo
            biometric_user = self.env['biometric.user'].search([('user_id', '=', user_id)], limit=1)
            if not biometric_user:
                biometric_user = self.env['biometric.user'].create({
                    'user_id': user_id,
                    'name': name,
                })

            _logger.info(f"Creating attendance record for User ID: {user_id}, Name: {name}, Timestamp: {timestamp}")
            self.env['biometric.attendance'].create({
                'user_id': biometric_user.id,
                'name': name,
                'timestamp': timestamp,
            })

        conn.disconnect()

    def sync_users(self):
        ip = self.ip_address
        port = self.port
        zk = ZK(ip, port=port, timeout=15)
        conn = zk.connect()

        # Retrieve users from the biometric device
        users = conn.get_users()

        # Process users
        for user in users:
            self.env['biometric.user'].create({
                'name': user.name,
                'user_id': user.user_id,
            })

        conn.disconnect()
