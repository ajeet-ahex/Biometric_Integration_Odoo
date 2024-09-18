{
    "name": "Attendance Biometric",
    "version": "17.0.1.0.1",
    "summary": """
        Attendance Biometric Integration.
    """,
    "category": "Customizations",
    "author": "Ahex Technologies Pvt Ltd",
    "license": "LGPL-3",
    "maintainers": [""],
    "website": "",
    "depends": [
        "base",
        "hr",
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/biometric_users.xml",
        "views/biometric.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False
}
