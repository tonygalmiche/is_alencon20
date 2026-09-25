# -*- coding: utf-8 -*-
{
    "name"     : "InfoSaône - Module Odoo 20 pour Alençon",
    "version"  : "20.0.0.1",
    "author"   : "InfoSaône",
    "category" : "InfoSaône",
    "description": """
InfoSaône - Module Odoo 20 pour Alençon
=======================================
Reprise d'is_alencon (Odoo 16) et de la partie THEIA d'is_plastigray16 (version 2023).
""",
    "maintainer" : "InfoSaône",
    "website"    : "http://www.infosaone.com",
    "depends"    : [
        "base",
        "mail",
        "hr",
        "web",
    ],
    "data" : [
        # is_plastigray16
        "security/res.groups.xml",
        "security/ir.access.csv",
        "views/is_database_view.xml",
        "views/is_equipement_view.xml",
        "views/is_theia_view.xml",
        "views/is_ilot_view.xml",
        "views/is_pointage_view.xml",
        "views/hr_view.xml",
        "views/is_mem_var_view.xml",
        "views/res_users_view.xml",
        "views/res_company_view.xml",
        "views/report_bilan_fin_of.xml",

        # is_alencon
        "views/is_theia_alencon_view.xml",
        "views/is_releve_qt_produite_view.xml",
        "views/menu.xml",
    ],
    "assets": {
        "web.assets_backend": [
            # "is_alencon20/static/src/parc_presse/*",  # JS Owl 2 : à migrer en Owl 3 avant de le réactiver
        ],
        "web.report_assets_common": [
            "is_alencon20/static/src/scss/report.scss",
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
