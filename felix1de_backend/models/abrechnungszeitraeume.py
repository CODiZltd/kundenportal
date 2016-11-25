# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

class backend_abrechnungszeitraeume(models.Model):
    _name='backend.abrechnungszeitraeume'
    _inherit='backend.apiais.accessid'
    
    abr_accessid=fields.Char('ID', compute='_lookup_accessid') 
    abr_name=fields.Char('Abrechnungszeitraum', compute='_abr_lookup_name')
    
    abrechnungszeitraum=fields.Char(String="Abrechnungszeitraum")
    abr_faelligkeit=fields.Char('Fälligkeit')
    abr_beschreibung=fields.Text('Beschreibung')
    
    @api.multi
    def _abr_lookup_name(self):
        for record in self:
            record.name = str(record.abrechnungszeitraum)