# -*- coding: utf-8 -*-

from odoo import models,fields


class is_badge(models.Model):
    _name='is.badge'
    _description="Badge"
    _order='employee'

    _name_uniq = models.Constraint('UNIQUE(name)', 'Ce badge existe déjà')

    name       = fields.Char(u"Code",size=20,required=True, index=True)
    employee   = fields.Many2one('hr.employee', u'Employé', required=False, ondelete='set null', help=u"Sélectionnez un employé")
    code_theia = fields.Char(u"Code Lecteur RFID THEIA",size=20, index=True)
    nom_odalid = fields.Char(u"Nom ODALID", help=u"Pour faire la correspondance entre Odoo et Odalid")
