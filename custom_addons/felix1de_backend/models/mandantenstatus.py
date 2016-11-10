# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_mandantenstatus(models.Model):
    _name='backend.mandantenstatus'
    
    name=fields.Char('Status')