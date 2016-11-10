# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_branchen(models.Model):
    _name='backend.branchen'
    
    name=fields.Char('Branche')
    kathegorie=fields.Char('Kathegorien')