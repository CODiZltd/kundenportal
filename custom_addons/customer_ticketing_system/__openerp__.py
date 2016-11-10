
{
    'name' : 'Felix1.de WebFrontend',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description' : """
Felix1.de WebFrontend Datenbankanwendung
=========================================
Datenbankanwendung zur Verwaltung der Felix1.de Niederlassungen, Mandanten und Kontakte 
und Integrationstool für die Unternehmenslogik.


    """,
    'version' : '1.0',
    'author' : 'GetOdoo, HiYACoding LTD',
   # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category' : 'Felix1.de WebFrontend',

    'website': 'http://www.getodoo.com, www.hiyacoding.co.uk',


    'images' : [],
    'depends' : ['base','mail','hr'],
    'data': [
       
        'security/ir.model.access.csv',
        'views/contact.xml',
        'views/customer_form_view.xml',
        'views/customer_ticketing_view.xml',
        'views/branch_view.xml',
        'views/contract_view.xml',
        'views/bank_details_view.xml',
        'security/ticket_security.xml',
        'views/ticket_employee_view.xml',
        'views/order_view.xml',
        'views/number_view.xml',
        'views/start_ticket.xml',
        'views/customer_mail_send_view.xml',
            ],
    'demo': ['demo/demo.xml'],
    'application': True,
    'installable': True,
    'auto_install': False,
}
