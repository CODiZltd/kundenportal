# -*- coding: utf-8 -*-
from openerp import http

# class BackendMapping(http.Controller):
#     @http.route('/backend_mapping/backend_mapping/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/backend_mapping/backend_mapping/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('backend_mapping.listing', {
#             'root': '/backend_mapping/backend_mapping',
#             'objects': http.request.env['backend_mapping.backend_mapping'].search([]),
#         })

#     @http.route('/backend_mapping/backend_mapping/objects/<model("backend_mapping.backend_mapping"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('backend_mapping.object', {
#             'object': obj
#         })