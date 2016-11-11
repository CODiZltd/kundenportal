# -*- coding: utf-8 -*-
from openerp import fields, models

class res_partner_mandanten_Kontakte(models.Model):

    _inherits = {
        'backend.mandanten': 'mandant_id',
        'backend.kontakte':'kontakt_id'
    }
    _inherit='res.partner'

    
    mandant_id = fields.Many2one('backend.mandanten', required=True,
           string="Related Mandanten", ondelete='restrict',
           help='Mandanten-related data of the User')
    #kontakt_id = fields.Many2one('backend.kontakte', required=False,
    #       string="Related Konbtakt", ondelete='restrict',
    #       help='Kontakte-related data of the User')
    
