# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_berater(models.Model):
    _name='backend.berater'
    
    name=fields.Char('Nachname', help="Name des Steuerberaters", required=True)
    bemerkung=fields.Text('Bemerkung')
    beraterid=fields.Integer('Berater ID')
    etlbenutzername=fields.Char('ETL Benutzername')
    vorname=fields.Char('Vorname', help="Vorname des Steuerberaters", required=True)
    anrede=fields.Selection([('Frau', 'Herr')])
    Titel=fields.Char('Titel')
    kanzleileiter=fields.Boolean('Kanzleileiter', dafault=False)
    ansprechpartner=fields.Boolean('Ansprechpartner',default=False)
    stb=fields.Boolean('StB', help="Steuerberater",default=False)
    stbln=fields.Boolean('StBln', help="SteuerberaterIn", default=False)
    ra=fields.Boolean('RA',help="Rechtsanwalt", default=False)
    wp=fields.Boolean('WP', help="??", default=False)
    weiteretitel=fields.Char('Weitere Titel')
    hochschulabschluss=fields.Char('Hochschulabschluss')
    foto=fields.Binary('Foto')
    vor_nach=fields.Char('Vorname, Nachname')
    nach_vor=fields.Char('Nachname, Vorname')
    tel1=fields.Char('Telefon1')
    tel2=fields.Char('Telefon2')
    tel3=fields.Char('Telefon3')
    email1=fields.Char('Email1')
    email2=fields.Char('Email2')
    email3=fields.Char('Email3')
    fax=fields.Char('Fax')
    datenok=fields.Char('Daten OK')
    
    