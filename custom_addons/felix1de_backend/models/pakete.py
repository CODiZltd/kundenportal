# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
 
class backend_pakete(models.Model):
    _name='backend.pakete'
    
    name=fields.Many2one("backend.paket", string="Paket")
    kategorie=fields.Many2one("backend.paketkategorie", string="Packetkathegorie")
    beschreibung=fields.Text("Beschreibung" )
    produktbild=fields.Binary("Produktbild")
    leistungserbringer=fields.Char('Leistungserbringer')#Many2one("backend.felix1gruppen", string="Leistungserbringer") 
    unternehmensformen=fields.Char('Unternehmensform')#One2many("backend.unternehmensformen","name", string="Unternehmensformen")#
    DerivatVon=fields.Many2one("backend.paket", string="DerivatVon")
    PreisAb=fields.Char("PreisAb")
    Bruttopreis=fields.Boolean("Bruttopreis", default=False)
    Standardgebuehr=fields.Monetary("Standardgebühr")
    Abrechnungszeitraum=fields.Many2one("backend.abrechnungszeitraeume", string="Abrechnungszeitraum")
    Produktseite=fields.Text("Produktseite")
    BestellLink=fields.Text("Bestell-Link")
    Checkliste=fields.Many2one('backend.checklistenvorlagen', string="Checkliste")
    Rechnungstext=fields.Char("Rechnungstext")
    Ident=fields.Boolean("Ident", default=False)
    Vollmacht=fields.Boolean("Vollmacht", default=False)
    pisa=fields.Boolean("PISA", default=False)
    sageone=fields.Boolean("SageOne", default=False)
    app=fields.Boolean("App", default=False)
    Besonderheiten=fields.Text("Besonderheiten")
    Status=fields.Many2one('backend.paketestatus', string="Paketestatus")#
    Mandantengruppe=fields.Integer("Mandantengruppe", default="0")
    WebsiteID=fields.Integer("WebsiteID")
    PreisSchluessel=fields.Many2one('backend.preiseschluessel', string="Preisschluessel")#
    DatenOK=fields.Boolean("DatenOK", default=False)
    currency_id=fields.Many2one('res.currency', string='Währung')
    
