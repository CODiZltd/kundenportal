# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_paketkategorie(models.Model):
    _name='backend.paketkategorie'
    
    name=fields.Char(String="Kategorie")
    description=fields.Text('Beschreibung')