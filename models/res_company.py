# -*- coding: utf-8 -*-

from odoo import models,fields,api


class res_company(models.Model):
    _inherit = 'res.company'

    is_mysql_pwd    = fields.Char('Mot de passe MySQL')
    is_dynacase_pwd = fields.Char('Mot de passe Dynacase')
    is_cpta_pwd     = fields.Char('Mot de passe AS400 CPTA')

    is_postgres_host = fields.Char('Serveur Postgres')
    is_postgres_user = fields.Char('Utilisateur Postgres')
    is_postgres_pwd  = fields.Char('Mot de passe Postgres')

    is_logo         = fields.Binary("Logo", help="Logo utilisé dans les documents (BL, facures,..)")
    bg_color        = fields.Char('Background color')
    text_color      = fields.Char('Text color')
    is_nb_threads   = fields.Integer('Nombre de coeurs à utiliser dans les programmes', default=1)

    is_url_intranet_odoo  = fields.Char('URL Intranet Odoo' , default='http://odoo')
    is_url_intranet_theia = fields.Char('URL Intranet THEIA', default='http://raspberry-cpi')
    is_url_odoo_theia     = fields.Char('URL Odoo THEIA')

    is_directeur_general_id      = fields.Many2one('res.users', u'Directeur Général'                     , help=u"Utilisé en particulier pour les DA Investissements")
    is_directeur_technique_id    = fields.Many2one('res.users', u'Directeur Technique'                   , help=u"Utilisé en particulier pour les DA Moules")
    is_acheteur_id               = fields.Many2one('res.users', u'Acheteur'                              , help=u"Utilisé en particulier pour transformer les SA en DAS")
    is_gest_demande_transport_id = fields.Many2one('res.users', u'Gestionnaire des demandes de transport', help=u"Utilisé pour envoyer un mail lors de la création d'une demande de transport")

    is_base_principale = fields.Boolean('Base principale (Primaire)', help="Cette case permet de masquer certains champs sur les bases répliquées si elle n'est pas cochée")

    is_code_societe      = fields.Char('Code société')
    is_dest_bilan_of_ids = fields.Many2many('res.users', 'is_res_company_users_rel', 'res_company_id','user_id', string="Destinataires du bilan de fin d'OF")
    is_cout_ctrl_qualite = fields.Float(u"Coût horaire vendu contrôle qualité", digits=(12, 2))

    is_dossier_interface_cegid = fields.Char(u"Dossier de destination pour le fichier d'interface de CEGID")

    is_sms_account  = fields.Char(u'SMS account')
    is_sms_login    = fields.Char(u'SMS login')
    is_sms_password = fields.Char(u'SMS password')
    is_sms_from     = fields.Char(u'SMS from')

    is_calendrier_expedition_id = fields.Many2one('res.partner', u'Calendrier Expéditions', domain=[('is_company','=',True),('is_adr_code','=','EXP')], help=u"Calendrier utilisé dans le calcul de la date d'expédition des commandes des clients (code adresse=EXP)")
    is_annee_pic_3ans           = fields.Char(u'Année PIC à 3 ans', help=u'Paramètre utilisé en particulier pour Analyse / Taux de rotation des stocks')
    is_cachet_plastigray        = fields.Binary("Cachet de Plastigray", help="Utilisé pour imprimer les certificats matière fournisseur")

    is_agenda_url = fields.Char(u'URL Google Agenda')
    is_agenda_pwd = fields.Char(u'Mot de passe admin Google Agenda')

    is_responsable_rh_id = fields.Many2one('res.users', string='Responsable RH')
    is_zebra_id = fields.Many2one('is.raspberry.zebra', u"Imprimante Zebra par défaut", help=u"Utilisé pour imprimer les étiquettes des équipements")

    is_activer_init = fields.Boolean('Activer les fonctions init des modèles', default=True, help="Désactiver cette option en mode développement pour accélérer la mise à jour du module")



    # THEIA : indicateurs du parc des presses et relevé des quantités produites (is_alencon)
    is_indicateur_ids             = fields.One2many('is.res.company.indicateur', 'company_id')
    is_affichage_indicateur_ids   = fields.One2many('is.res.company.indicateur.affichage', 'company_id')
    is_coeff_tx_rebut_parc        = fields.Float('Coefficient Taux de rebut parc', digits=(14,2), default=1)
    is_dossier_releve_qt_produite = fields.Char("Dossier 'Relevé des qt produites'")

    def write(self, vals):
        base_group_id = self.env.ref('base.group_user')
        principale_grp_id = self.env.ref('is_plastigray16.is_base_principale_grp')
        secondaire_grp_id = self.env.ref('is_plastigray16.is_base_secondaire_grp')
        if vals and vals.get('is_base_principale'):
            principale_grp_id.write({'users': [(4, user) for user in base_group_id.users.ids]})
            secondaire_grp_id.write({'users': [(5, user) for user in base_group_id.users.ids]})
        if vals.get('is_base_principale') == False:
            secondaire_grp_id.write({'users': [(4, user) for user in base_group_id.users.ids]})
            principale_grp_id.write({'users': [(5, user) for user in base_group_id.users.ids]})
        return super(res_company, self).write(vals)


    def annee_pic_3ans_action(self):
        for obj in self:
            self.env['is.taux.rotation.stock.new'].annee_pic_3ans_action()


class res_partner_bank(models.Model):
    _inherit = 'res.partner.bank'

    is_bank_swift = fields.Char('Code swift')


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
