# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_kanzleien(models.Model):
    _name='backend.kanzleien'
    
    niederlassung=fields.Char(String="Niederlassung", help="Name des Niederlassung")
    bemerkung=fields.Text()
    f1kanzleinummer=fields.Integer('f1KanzleiNummer')
    hausnr=fields.Char('Hausnr.:')
    str=fields.Char('Straße')
    str2=fields.Char('Straße-Zusatz')
    plz=fields.Integer('PLZ')
    ort=fields.Char('Ort')
    ort2=fields.Char('Ort-Zusatz')
    email=fields.Char('Email')
    vertragsart=fields.Char('Vertragsart')
    ETAXBeraternummer=fields.Integer('ETAXBeraternummer')
    Lohnberaternummer=fields.Integer('Lohnberaternummer')
    reweTestkanzlei=fields.Boolean('reweTestkanzlei')
    SageAcCEdition=fields.Boolean('Sage AcC Edition')
    virtuellesETAX=fields.Char('virtuelles ETAX')
    etlnummerstamm=fields.Integer('ETL Nummer Stammkanzlei')
    name=fields.Char('Name Stammkanzlei')
    ortstammkanzlei=fields.Char('Ortstammkanzlei')
    datenok=fields.Char('Daten OK')
    beitragmonat=fields.Char("Beitrag monatlich")
    beitragjahr=fields.Char("Beitrag jährlich")
    beitragmonatredox=fields.Char("Beitrag monatlich reduziert")
    beitragjahrredox=fields.Char("Beitrag jährlich reduziert")
    startdatum=fields.Char('Startdatum')
    kundigungdatum=fields.Char('Kündigungsdatum')
    ausgesetztbis=fields.Char('Ausgesetzt Bis')
    scsbereich=fields.Char('SCSBereich')
    