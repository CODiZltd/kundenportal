# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
 
class backend_lohnpreiseartikel(models.Model):
    _name='backend.lohnpreiseartikel'
    
    Produktkategorie=fields.Integer("Produktkategorie")
    PreiseSchluesselSchluessel=fields.Integer('PreiseSchluesselSchluessel')
    ArtikelLohnNummer=fields.Char('ArtikelLohnNummer')
    Preis=fields.Monetary('Preis')
    name=fields.Char('ArtikelLohnName')
    ETLNrPKC=fields.Integer('ETLNrPKC')
    Erloeskonto=fields.Char('Erloeskonto')
    Zahlungsweise=fields.Char('Zahlungsweise')
    Beschreibung=fields.Char('Beschreibung')
    currency_id=fields.Many2one('res.currency',string='Währung')
    
    
