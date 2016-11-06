# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_kontakte(models.Model):
    _name='backend.kontakte'
    
    vorname=fields.Char("Vorname")
    name=fields.Char("Nachname")
    anrede=fields.Char("Anrede")
    titel=fields.Char("Titel") #.(selection=[('Dr.', 'Dr.'),('Prof.','Prof.'),('Prof. Dr.','Prof. Dr.')])
    vornamenachname=fields.Char('Vorname Nachname')
    nachnamevorname=fields.Char('Nachname Vorname')
    telefon1=fields.Char("Telefon1")
    telefon2=fields.Char("Telefon2")
    telefon3=fields.Char("Telefon3")
    email1=fields.Char("eMail1")
    email2=fields.Char("eMail2")
    email3=fields.Char("eMail3")
    fax=fields.Char("Fax")
    bemerkung=fields.Char("Bemerkung")
    vip=fields.Boolean("VIP", default=False)
    strasse=fields.Char("Strasse")
    hausnummer=fields.Char("Hausnummer")
    plz=fields.Char("PLZ")
    ort=fields.Char("Ort")
    bundesland=fields.Char("Bundesland")    #selection=[('bw', 'Baden-Württemberg'),
                                            #('bay','Bayern'),
                                            #('bln','Berlin'),
                                            #('Bbg', 'Brandenburg'),
                                            #('bre', 'Bremen'),
                                            #('ham', 'Hamburg'),
                                            #('hes', 'Hessen'),
                                            #('mvp', 'Mecklrnburg-Vorpommern'),
                                            #('nie', 'Niedersachsen'),
                                            #('nrw', 'Nordrhein-Westfalen'),
                                            #('rpf', 'Rheinland-Pfalz'),
                                            #('sar', 'Saarland'),
                                            #('sax', 'Sachsen'),
                                            #('saa', 'Sachsen-Anhalt'),
                                            #('sle', 'Schleswig-Holstein'),
                                            #('thü', 'Thüringen')])
    land=fields.Char("Land")
    addresse=fields.Char('Adresse')
    datenok=fields.Boolean("DatenOK", default=False)
     

   # @api.onchange('plz')
   # def _auto_adresse(self):
   #     self.addresse = str(self.strasse) + " " + str(self.hausnummer) + ", " + self.plz + " " + self.ort
   # 
   # @api.onchange('name', 'vorname')
   # def _auto_namevorname(self):
   #     # set auto-changing field
   #     self.nachnamevorname = str(self.name) + ", " + str(self.vorname)
   # 
   # @api.onchange('vorname', 'name')
   # def _auto_vornamename(self):
   #     self.vornamenachname = str(self.vorname) + ", " + str(self.name)
        # Can optionally return a warning and domains
        #return {
        #    'warning': {
        #        'title': "Something bad happened",
        #        'message': "It was very bad indeed",
        #            }
        #        }