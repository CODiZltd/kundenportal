# -*- coding: utf-8 -*-
from openerp import fields, models

class res_partner_mandanten(models.Model):
    #_name= 'openacademy.partner'
    _inherits = {'backend.mandanten': 'mandant_id'}
    _inherit='res.partner'
    #_inherit='backend.mandanten'
    #_inherits = {'backend.mandanten': 'mandanten_id'}
    
    mandant_id = fields.Many2one('backend.mandanten', required=True,
           string="Related Mandanten", ondelete='restrict',
           help='Mandanten-related data of the User')
    
    #name=fields.Char('Partner ID')
    #name=fields.Many2one('res.partner', ondelete='cascade', required=True)
    #namen=fields.Many2one('res.partner','partner_id')
    # Add a new column to the res.partner model, by default partners are not
    # instructorsfff
    instructor = fields.Boolean("Instructor", default=False)
    email=fields.Char('email', required=False)


