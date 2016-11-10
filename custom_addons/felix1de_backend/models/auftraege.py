# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_auftraege(models.Model):
    _name='backend.auftraege'
    
    name=fields.Many2one("backend.mandanten", string="Mandant",Index=True)
    buchungsdatum=fields.Date("Buchungsdatum")
    Paket=fields.Many2one("backend.pakete", string="Pakete", Index=True)
    Start=fields.Date("Start")
    Ende=fields.Date("Ende")
    Umsatz=fields.Monetary("Umsatz")
    Bruttoeinnahmen=fields.Monetary("Bruttoeinnahmen")
    Arbeitnehmer=fields.Integer("Arbeitnehmer")
    GebuehrMonatSonst=fields.Monetary("GebuehrMonatSonst")
    GebuehrMonatBetriebSt=fields.Monetary("GebuehrMonatBetriebSt")
    GebuehrMonatFiBu=fields.Monetary("GebuehrMonatFiBu")
    GebuehrMonatFiBuUeberw=fields.Monetary("GebuehrMonatFiBuUeberw")
    GebuehrEinmalSonst=fields.Monetary("GebuehrEinmalSonst")
    GebuehrEinmalBetriebSt=fields.Monetary("GebuehrEinmalBetriebSt")
    GebuehrEinmalFiBu=fields.Monetary("GebuehrEinmalFiBu")
    GebuehrEinmalFiBuUeberw=fields.Monetary("GebuehrEinmalFiBuUeberw")
    GebuehrJahrSonst=fields.Monetary("GebuehrJahrSonst")
    GebuehrJahrBetriebSt=fields.Monetary("GebuehrJahrBetriebSt")
    GebuehrJahrFiBu=fields.Monetary("GebuehrJahrFiBu")
    GebuehrJahrFiBuUeberw=fields.Monetary("GebuehrJahrFiBuUeberw")
    GebuehrMonat=fields.Monetary("GebuehrMonat")
    GebuehrEinmal=fields.Monetary("GebuehrEinmal")
    GebuehrJahr=fields.Monetary("GebuehrJahr")
    Bemerkung=fields.Text("Bemerkung")
    Start1=fields.Date("Start1")
    Ende1=fields.Date("Ende1")
    Umsatz1=fields.Monetary("Umsatz1")
    Bruttoeinnahmen1=fields.Monetary("Bruttoeinnahmen1")
    Arbeitnehmer1=fields.Integer("Arbeitnehmer1")
    GebuehrMonatSonst1=fields.Monetary("GebuehrMonatSonst1")
    GebuehrMonatBetriebSt1=fields.Monetary("GebuehrMonatBetriebSt1")
    GebuehrMonatFiBu1=fields.Monetary("GebuehrMonatFiBu1")
    GebuehrMonatFiBuUeberw1=fields.Monetary("GebuehrMonatFiBuUeberw1")
    GebuehrEinmalSonst1=fields.Monetary("GebuehrEinmalSonst1")
    GebuehrEinmalBetriebSt1=fields.Monetary("GebuehrEinmalBetriebSt1")
    GebuehrEinmalFiBu1=fields.Monetary("GebuehrEinmalFiBu1")
    GebuehrEinmalFiBuUeberw1=fields.Monetary("GebuehrEinmalFiBuUeberw1")
    GebuehrJahrSonst1=fields.Monetary("GebuehrJahrSonst1")
    GebuehrJahrBetriebSt1=fields.Monetary("GebuehrJahrBetriebSt1")
    GebuehrJahrFiBu1=fields.Monetary("GebuehrJahrFiBu1")
    GebuehrJahrFiBuUeberw1=fields.Monetary("GebuehrJahrFiBuUeberw1")
    FiBuAufSage=fields.Boolean("FiBuAufSage", default=False)
    FiBuAufSage1=fields.Boolean("FiBuAufSage1", dafault=False)
    Ersteller=fields.Char("Ersteller")
    AngelegtAm=fields.Date("AngelegtAm")
    AngelegtVon=fields.Char("AngelegtVon")
    Auftragswert=fields.Monetary("Auftragswert")
    DatenOK=fields.Boolean("DatenOK", default=False)
    currency_id=fields.Many2one('res.currency', string="Währung")