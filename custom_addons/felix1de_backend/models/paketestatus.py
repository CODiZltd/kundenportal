# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_paketestatus(models.Model):
    _name='backend.paketestatus'
    
    name=fields.Char(String="Paketestatus")
    description=fields.Text('Beschreibung')