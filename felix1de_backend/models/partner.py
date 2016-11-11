# -*- coding: utf-8 -*-
from openerp import fields, models

class res_partner_mandanten(models.Model):
    #_name= 'openacademy.partner'
    _inherit='res.partner'
    _inherits = {
        'backend.mandanten': 'mandant_id',
    }

    #_inherit='backend.mandanten'
    #_inherits = {'backend.mandanten': 'mandanten_id'}
    
    mandant_id = fields.Many2one('backend.mandanten', required=True,
           string="Related Mandanten", ondelete='restrict',
           help='Mandanten-related data of the User')



    manname=fields.Many2one('backend.mandanten')