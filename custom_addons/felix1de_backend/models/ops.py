# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_ops(models.Model):
    _name='backend.ops'
    
    OpID=fields.Char('OpID')
    name=fields.Char('OpName')
    OpInhaber=fields.Char('OpInhaber')
    AccountName=fields.Char('AccountName')
    Erstelldatum=fields.Date('Erstelldatum')
    Schlusstermin=fields.Date('Schlusstermin')
    Phasendauer=fields.Integer('Phasendauer')
    Kampagne=fields.Char('Kampagne')
    LeadQuelle=fields.Char('LeadQuelle')
    status=fields.Char('Status')
    Wert=fields.Monetary('Wert')
    Branche=fields.Char('Branche')
    MandantenNr=fields.Char('MandantenNr')
    beschreibung=fields.Text('Beschreibung')
    currency_id=fields.Many2one('res.currency',string='Währung')