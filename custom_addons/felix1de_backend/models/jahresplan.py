# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_AAA_Jahresplan(models.Model):
    _name='backend.jahresplan'
    
    name=fields.Char('KoopPartner', required=True)
    jan=fields.Text('Januar')
    feb=fields.Text('Februar')
    mar=fields.Text('März')
    apr=fields.Text('April')
    mai=fields.Text('Mai')
    jun=fields.Text('Juni')
    jul=fields.Text('Juli')
    aug=fields.Text('August')
    sep=fields.Text('September')
    okt=fields.Text('Oktober')
    nov=fields.Text('November')
    dez=fields.Text('Dezember')
   
    