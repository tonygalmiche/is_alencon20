# -*- coding: utf-8 -*-
from odoo import models,fields


class is_ilot(models.Model):
    _name='is.ilot'
    _description="is_ilot"
    _order='name'
    name    = fields.Char("Ilot", required=True)
    atelier = fields.Selection([('Injection', 'Injection'), ('Assemblage', 'Assemblage')], 'Atelier')
