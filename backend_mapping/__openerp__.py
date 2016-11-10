# -*- coding: utf-8 -*-
{
    'name': "backend_mapping",
    'summary': """
         Anbindung der Access Datenbank an Odoo""",

    'description': """
        Die Access Tabellen werden an das Odoo-Framework angebunden. 
    """,

    'author': "HiYa Coding LTD",
    'website': "http://www.hiyacoding.co.uk",
    'icon': "/felix1de_backend/static/description/backend.png",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'felix1de',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','hr'],

    # always loaded
    'data': [
     #'security/ir.model.access.csv',
     #'views/contact.xml',
     #'views/customer_form_view.xml',
     #'views/customer_ticketing_view.xml',
     #'views/branch_view.xml',
     #'views/contract_view.xml',
     #'views/bank_details_view.xml',
     #'security/ticket_security.xml',
     #'views/ticket_employee_view.xml',
     #'views/order_view.xml',
     #'views/number_view.xml',
     #'views/start_ticket.xml',
     #'views/customer_mail_send_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False
}