# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_felix1gruppen(models.Model):
    _name='backend.felix1gruppen'
    
    name=fields.Char(String="Gruppe")
    description=fields.Text('Beschreibung')