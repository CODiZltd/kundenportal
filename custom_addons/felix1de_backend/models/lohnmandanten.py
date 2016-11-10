# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_lohnmandanten(models.Model):
    _name='backend.lohnmandanten'
    
    name=fields.Char('Mandantennummer')
    edlohnBeraternummer=fields.Char('edlohnBeraternummer')
    edlohnMandantennummer=fields.Char('edlohnMandantennummer')
    Zahlungsweise=fields.Char('Zahlungsweise')
    abweichenderAbrechnungsmonat=fields.Char('abweichenderAbrechnungsmonat')
    Zusatzprodukt=fields.Integer('Zusatzprodukt')
    GlaubigerID=fields.Char('GlaubigerID')
    Debitorennummeredfibu=fields.Char('Debitorennummeredfibu')
    beschreibung=fields.Text('Beschreibung')
    