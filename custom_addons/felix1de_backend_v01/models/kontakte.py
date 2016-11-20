# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_kontakte(models.Model):
    _name='backend.kontakte'
    
    firsn=fields.Char("Vorname")
    name=fields.Char("Nachname")
    anrede=fields.Char("Anrede")
    title=fields.Char("Titel")
    vornach=fields.Char("VornameNachname")
    nachvor=fields.Char("NachnameVorname")
    tel1=fields.Char("Telefon1")
    tel2=fields.Char("Telefon2")
    tel3=fields.Char("Telefon3")
    email1=fields.Char("eMail1")
    email2=fields.Char("eMail2")
    email3=fields.Char("eMail3")
    fax=fields.Char("Fax")
    bemerkung=fields.Char("Bemerkung")
    VIP=fields.Boolean("VIP", default=False)
    str=fields.Char("Strasse")
    hausnummer=fields.Char("Hausnummer")
    plz=fields.Char("PLZ")
    ort=fields.Char("Ort")
    bundeslands=fields.Char("Bundesland")
    land=fields.Char("Land")
    addresse=fields.Char("Adresse")
    datenok=fields.Boolean("DatenOK", default=False)
    
  
