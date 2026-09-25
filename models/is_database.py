# -*- coding: utf-8 -*-
from odoo import api,fields,models,tools,SUPERUSER_ID
import logging
_logger = logging.getLogger(__name__)


class is_database(models.Model):
    _name = 'is.database'
    _description = "Database"
    _order='name'

    name                   = fields.Char('Site'           , required=True)
    ip_server              = fields.Char('Adresse IP'     , required=False)
    port_server            = fields.Integer('Port'        , required=False)
    database               = fields.Char('Base de données', required=False)
    login                  = fields.Char('Login'          , required=False)
    password               = fields.Char('Mot de passe'   , required=False)
    is_database_origine_id = fields.Integer("Id d'origine", readonly=True)
