# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_checklistenvorlagen(models.Model):
    _name='backend.checklistenvorlagen'
    
    name=fields.Char(String="Bezeichnung")
    typ=fields.Many2one("backend.checklistentypen", string="Typ")
    beschreibung=fields.Text('Beschreibung')