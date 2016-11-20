# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_abrechnungszeitraeume(models.Model):
    _name='backend.abrechnungszeitraeume'
    
    name=fields.Char(String="Abrechnungszeitraum")
    faelligkeit=fields.Char("Fälligkeit")
    beschreibung=fields.Text('Beschreibung')