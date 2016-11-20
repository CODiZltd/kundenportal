from openerp import models, fields, api,_

class backend_auftraege(models.Model):
    _inherit='backend.auftraege'
    
    product_id=fields.One2many('backend.line', 'line')
   
	
   
class backend_auftraege(models.Model):
    _name='backend.line'
    
    line=fields.Many2one('backend.auftraege')
    name=fields.Char('Name')
    monatsgebuhr=fields.Float('Monatsgebuhr')
    einmalgebuhr=fields.Float('Einmalgebuhr')
    jahresgebuhr=fields.Float('Jahresgebuhr')
    order_id=fields.Many2one('client.order')
    
