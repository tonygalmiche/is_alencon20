# -*- coding: utf-8 -*-

from odoo import models,fields,api


class hr_employee(models.Model):
    _inherit = "hr.employee"
    _rec_names_search = ['name', 'is_matricule']

    def _badge_count(self):
        badge_obj = self.env['is.badge']
        for obj in self:
            nb = len(badge_obj.search([('employee', '=', obj.id)]))
            obj.is_badge_count=nb

    is_matricule=fields.Char('Matricule', help='N° de matricule du logiciel de paye', required=False)
    is_categorie=fields.Selection([
            ("2x8" , "Équipe en 2x8"), 
            ("2x8r", "Équipe en 2x8 avec recouvrement"), 
            ("nuit", "Équipe de nuit"),
            ("3x8" , "en 3x8"),
            ("jour", "Personnel de journée"),
        ], "Catégorie de personnel", required=False)
    is_interimaire    = fields.Boolean('Intérimaire',  help="Cocher pour indiquer que c'est un intérimaire")
    is_badge_count    = fields.Integer('# Badges'      , compute='_badge_count'   , readonly=True, store=False)
    is_jour1=fields.Float('Lundi')
    is_jour2=fields.Float('Mardi')
    is_jour3=fields.Float('Mercredi')
    is_jour4=fields.Float('Jeudi')
    is_jour5=fields.Float('Vendredi')
    is_jour6=fields.Float('Samedi')
    is_jour7=fields.Float('Dimanche')

    message_main_attachment_id = fields.Many2one(groups="base.group_user") # Etait : groups="hr.group_hr_user"


    def _compute_display_name(self):
        super()._compute_display_name()
        for obj in self:
            obj.display_name = "%s (%s)"%(obj.name,(obj.is_matricule or ''))
