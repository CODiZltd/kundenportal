# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_mandanten(models.Model):
    _name='backend.mandanten'
    
    man_accessid=fields.Char('ID', compute='_lookup_accessid')
    name=fields.Char('Mandant', compute='_man_lookup_name')
    
    mandant=fields.Char(string="Mandant", help="Name des Mandanten", required=True)
    mandantennummer=fields.Char('Mandantennummer',required=True, index=True)
    man_bemerkung=fields.Text("Bemerkung") 
    man_emailpisa=fields.Char(string="eMailPISA")
    man_kanzlei=fields.Many2one('backend.kanzleien', ondelete='restrict', string="Kanzlei", index=True)
    man_steuerberater=fields.Many2one('backend.berater', ondelete='restrict', string="Steuerberater", index=True)
    man_unternehmensform=fields.Many2one('backend.unternehmensformen', ondelete='restrict', string="Unternehmensform", index=True)
    man_branche=fields.Many2one('backend.branchen', ondelete='restrict', string="Branche")
    man_status=fields.Many2one('backend.mandantenstatus', ondelete='restrict', index=True)
    man_empfaenger1=fields.Char("Empfänger 1")
    man_empfaenger2=fields.Char("Empfänger 2")
    man_strasse=fields.Char('Straße')
    man_hausnummer=fields.Char("Hausnummer")
    man_plz=fields.Char("PLZ")
    man_ort=fields.Char("Ort")
    man_bundesland=fields.Char("Bundesland")
    #man_land=fields.Char("Land")
    man_adresse=fields.Char("Adresse")
    man_bankname=fields.Char('Bank')
    man_bic=fields.Char('BIC')
    man_iban=fields.Char('IBAN')
    man_kontoinhaber=fields.Char('Kontoinhaber')
    man_telefon1=fields.Char('Telefon1')
    man_telefon2=fields.Char('Telefon2')
    man_email1=fields.Char('Email1')
    man_email2=fields.Char('Email2')
    man_datenok=fields.Boolean('Daten OK',default=False)
    
    @api.multi
    def _man_lookup_name(self):
        for record in self:
            record.name = str(record.mandant)
    
    @api.multi
    def _lookup_accessid(self):
        for record in self:
            record.man_accessid = str(record.id)
            
