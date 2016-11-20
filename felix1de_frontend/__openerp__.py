# -*- coding: utf-8 -*-
{
    'name': "felix1.de Kundenportal",

    'summary': """
        felix1.de Webanwendung und Datenbank Frontend""",

    'description': """
        Dieses Modul ersetzt die bisherige MS Access Anwendung.
        Das Kundenportal wurde um die folgende Funktionen erweitert:
        
        - Ticketmanagement (Ticketverwaltung für Manager)
        - Unternehmenskomunikation (intern/extern)
        - Mitarbeiterverwaltung
   """,

    'author': "HiYa Coding LTD",
    'website': "http://www.hiyacoding.co.uk",
    'icon': "/felix1de_frontend/static/description/portal.png",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'felix1.de',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False
}