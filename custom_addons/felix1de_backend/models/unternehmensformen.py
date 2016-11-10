# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_unternehmensformen(models.Model):
    _name='backend.unternehmensformen'
    
    name=fields.Char("Unternehmensform")