# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenStow Technologies, 
#    Copyright (C) 2010-2015 (www.openstow.com)
#
#    This program is developed and maintain by GetOpenERP.
#
###############################################################################
{
    "name": "Custom Mail Send",
    "version": "2.0",
    "sequence": 1,
    "author": "GetOpenERP (Part of OpenStow Technologies)",
    "category": "Mail Customization",
    "description": """
This module is for customization 
----------------------
* Mail Send. 

    """,
    "website": "https://www.getopenerp.com",
    "depends": ["base", 'mail','customer_ticketing_system'],
    "demo": [],
    "data": ['new_custom_mail_send_view.xml',
             'res_partner_view.xml',  
            
    ],
    "installable": True,
    "auto_install": False,
    "active": False
}
