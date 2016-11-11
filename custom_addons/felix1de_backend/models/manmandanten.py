# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_apiais_accessid(models.Model):
    _name='backend.apiais.manaccessid'
    
    @api.multi
    def _lookup_manaccessid(self):
        for record in self:
            record.manaccessid = str(record.id)

class backend_mandanten(models.Model):
    _name='backend.manmandanten'
    _inherit='backend.apiais.manaccessid'
    
    manaccessid=fields.Char('ID', compute='_lookup_accessid')
    manname=fields.Char(String="Mandant", help="Name des Mandanten", required=True)
    manbemerkung=fields.Text()
    manmandantennummer=fields.Char('Mandantennummer',required=True, index=True) 
    manemailpisa=fields.Char(String="eMailPISA")
    mankanzlei=fields.Many2one('backend.kanzleien', ondelete='set null', String="Kanzlei", index=True)
    mansteuerberater=fields.Many2one('backend.berater', ondelete='set null', String="Steuerberater", index=True)
    manunternehmensform=fields.Many2one('backend.unternehmensformen', ondelete='set null', String="Unternehmensform", index=True)
    manbranche=fields.Many2one('backend.branchen', ondelete='set null', String="Branche")
    manstatus=fields.Many2one('backend.mandantenstatus', ondelete='set null', index=True)
    manempfaenger1=fields.Char()
    manempfaenger2=fields.Char()
    manstrasse=fields.Char('Straße')
    manhausnummer=fields.Char()
    manplz=fields.Char()
    manort=fields.Char()
    manbundesland=fields.Char()
    manland=fields.Char()
    manadresse=fields.Char()
    manbankname=fields.Char('Bank')
    manbic=fields.Char('BIC')
    maniban=fields.Char('IBAN')
    mankontoinhaber=fields.Char('Kontoinhaber')
    mantelefon1=fields.Char('Telefon1')
    mantelefon2=fields.Char('Telefon2')
    manemail1=fields.Char('Email1')
    manemail2=fields.Char('Email2')
    mandatenok=fields.Boolean('Daten OK',default=False)
    
    
    
