# -*- coding: utf-8 -*-
{
    'name': "Setting Sample",

    'summary': """
        Adding Field to General Settings Sample""",

    'description': """
        Adding Field to General Settings Sample
    """,

    'author': "PS-US Odoo",
    'website': "http://www.yourcompany.com",

    'category': 'Custom Development',
    'version': '0.1',
    'license': 'OEEL-1',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        'views/res_config_settings_views.xml',
    ],
}
