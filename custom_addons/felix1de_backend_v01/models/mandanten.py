# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_mandanten(models.Model):
    _name='backend.mandanten'
    
    name=fields.Char(String="Mandant", help="Name des Mamdanten", required=True)
    bemerkung=fields.Text()
    mandantennummer=fields.Integer('Mandantennummer',required=True, Index=True) 
    emailpisa=fields.Char(String="eMailPISA")
    kanzlei=fields.Many2one('backend.kanzleien', ondelete='set null', String="Kanzlei", Index="True")
    steuerberater=fields.Many2one('backend.berater', ondelete='set null', String="Steuerberater", Index="True")
    unternehmensform=fields.Many2one('backend.unternehmensformen', ondelete='set null', String="Unternehmensform", Index="True")
    branche=fields.Many2one('backend.branchen', ondelete='set null', String="Branche")
    status=fields.Many2one('backend.mandantenstatus', ondelete='set null')
    empfaenger1=fields.Char()
    empfaenger2=fields.Char()
    strasse=fields.Char('Straße')
    hausnummer=fields.Char()
    plz=fields.Char()
    ort=fields.Char()
    bundesland=fields.Char()
    land=fields.Char()
    addresse=fields.Char()
    bankname=fields.Char('Bank')
    bic=fields.Char('BIC')
    iban=fields.Char('IBAN')
    kontoinhaber=fields.Char('Kontoinhaber')
    tel1=fields.Char('Telefon1')
    tel2=fields.Char('Telefon2')
    email1=fields.Char('Email1')
    email2=fields.Char('Email2')
    datenok=fields.Boolean('Daten OK')
    
