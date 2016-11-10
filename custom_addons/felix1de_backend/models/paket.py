# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_paket(models.Model):
    _name='backend.paket'
    
    name=fields.Char(String="Paket")
    description=fields.Text('Beschreibung')