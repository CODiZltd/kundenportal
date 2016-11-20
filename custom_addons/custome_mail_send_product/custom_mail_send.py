# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime, timedelta
from openerp import SUPERUSER_ID
from openerp import api, fields, models, _
import openerp.addons.decimal_precision as dp
from openerp.exceptions import UserError
from openerp.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT


class res_partner(models.Model):
    _inherit = 'felix1.ticket'
    
    partner_id = fields.Many2one('res.partner',ondelete='cascade',required=True)
    
    @api.multi
    def action_emails_sends(self):
        '''
        This function opens a window to compose an email, with the edi respartner template message loaded by default
        '''
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('custome_mail_send_product', 'email_template_auto_customer_partner122')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = dict()
        ctx.update({
            'default_model': 'felix1.ticket',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True
        })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }


class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'
   
    
    @api.multi
    def send_mail(self, auto_commit=False):
        if self._context.get('default_model') == 'felix1.ticket' and self._context.get('default_res_id') and self._context.get('mark_so_as_sent'):
            order = self.env['felix1.ticket'].browse([self._context['default_res_id']])
            return super(MailComposeMessage, self.with_context(mail_post_autofollow=True)).send_mail(auto_commit=auto_commit)
   
               






