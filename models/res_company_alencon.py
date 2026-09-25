# -*- coding: utf-8 -*-
from odoo import models,fields,api


class res_company(models.Model):
    _inherit = 'res.company'

    is_indicateur_ids             = fields.One2many('is.res.company.indicateur', 'company_id')
    is_affichage_indicateur_ids   = fields.One2many('is.res.company.indicateur.affichage', 'company_id')
    is_coeff_tx_rebut_parc        = fields.Float('Coefficient Taux de rebut parc', digits=(14,2), default=1)
    is_dossier_releve_qt_produite = fields.Char("Dossier 'Relevé des qt produites'")


class is_res_company_indicateur(models.Model):
    _name        = "is.res.company.indicateur"
    _description = "Couleurs des indicateurs pour THEIA"
    _order = "sequence"

    company_id = fields.Many2one("res.company", string="Société", required=True, ondelete='cascade')
    sequence   = fields.Integer(string="Ordre")
    limite     = fields.Float(string="Limite", digits=(14,2), help="Couleur de cet indicateur à partir de cette limite")
    indicateur = fields.Selection([
        ("tx_avance"    , "Avancement du Lancement"),
        ("tx_cycle"     , "Taux de Cycle"),
        ("tx_fct"       , "Taux de fonctionnement"),
        ("tx_rebut"     , "Taux de Rebut"),
        ("tx_cycle_parc", "Taux de Cycle Parc"),
        ("tx_fct_parc"  , "Taux de fonctionnement Parc"),
        ("tx_rebut_parc", "Taux de Rebut Parc"),
    ], string="Indicateur")
    color = fields.Char("Couleur")


class is_res_company_indicateur_affichage(models.Model):
    _name        = "is.res.company.indicateur.affichage"
    _description = "Affichage des indicateurs pour THEIA"
    _order = "sequence"

    company_id = fields.Many2one("res.company", string="Société", required=True, ondelete='cascade')
    sequence   = fields.Integer(string="Ordre")
    etat_id    = fields.Many2one("is.etat.presse", string="Etat", required=True)
    tx_avance  = fields.Boolean(string="Avancement du Lancement", default=True)
    tx_cycle   = fields.Boolean(string="Taux de Cycle", default=True)
    tx_fct     = fields.Boolean(string="Taux de fonctionnement", default=True)
    tx_rebut   = fields.Boolean(string="Taux de Rebut", default=True)
