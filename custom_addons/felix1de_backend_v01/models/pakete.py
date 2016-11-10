# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
 
class backend_pakete(models.Model):
    _name='backend.pakete'
    
    name=fields.Char(String="paket", help="Access Backend Version", readonly=True)
    description=fields.Text()
