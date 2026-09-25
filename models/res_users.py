# -*- coding: utf-8 -*-
from odoo import models,fields,api, SUPERUSER_ID
from odoo.http import request
from datetime import datetime


class is_res_users(models.Model):
    _name = 'is.res.users'
    _description="is_res_users"
    _order= 'heure_connexion desc'

    user_id         = fields.Many2one('res.users', 'Utilisateur', index=True)
    heure_connexion = fields.Datetime('Heure de connexion'      , index=True)
    adresse_ip      = fields.Char('Adresse IP'                  , index=True)


class res_users(models.Model):
    _inherit = "res.users"

    is_adresse_ip = fields.Char('Adresse IP', help='Adresse IP de cet utilisateur pour lui donner des accès spcécifiques dans THEIA')


    def _login(self, credential, user_agent_env):
        "Permet d'ajouter l'adresse IP de la personne qui se connecte cela est utilise par les programmes externes"
        auth_info = super()._login(credential, user_agent_env)
        try:
            ip = request.httprequest.environ['REMOTE_ADDR']
        except Exception:
            ip = False
        with self.pool.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            vals={
                'user_id'        : auth_info.get('uid'),
                'heure_connexion': datetime.now(),
                'adresse_ip'     : ip,
            }
            env['is.res.users'].create(vals)
        return auth_info
