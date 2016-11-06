# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_checklistentypen(models.Model):
    _name='backend.checklistentypen'
    
    name=fields.Char(String="Bezeichnung")
    description=fields.Text('Beschreibung')