# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_preiseschluessel(models.Model):
    _name='backend.preiseschluessel'
    
    beschreibung=fields.Text('Beschreibung')
    name=fields.Char('Schlüssel')
    abrechnungszeitraum=fields.Many2one('backend.abrechnungszeitraeume', string='Abrechnungszeitraum')#
    istBruttopreis=fields.Boolean('IstBruttopreis', default=False)
    MehrfachBuchbar=fields.Boolean('MehrfachBuchbar', help="gilt z.B. für Lohnabrechnung", default=False)
    provision=fields.Monetary('Provision')
    currency_id=fields.Many2one('res.currency', string="Währung")
    