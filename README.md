# is_alencon20

Module Odoo 20 pour Alençon. Il reprend `is_alencon` (Odoo 16) et **uniquement** la partie THEIA d'`is_plastigray16` (version 2023) dont il a besoin. Il n'y a plus de dépendance à `is_plastigray16`.

Plan de migration : `Documentation/migration-odoo/migration-is_alencon16-vers-is_alencon20.md`.

## Étape 1 : copie à l'identique (non installable en l'état)

- Les fichiers d'`is_plastigray16` gardent leur nom.
- Les fichiers d'`is_alencon` dont le nom existait déjà reçoivent le suffixe `_alencon` : `models/is_theia_alencon.py`, `models/res_company_alencon.py`, `views/is_theia_alencon_view.xml`, `views/res_company_alencon_view.xml`, `views/menu_alencon.xml`, `security/ir.model.access.alencon.csv`. Ils héritent des fichiers sans suffixe, et sont donc chargés après eux. Ils seront fusionnés dans leur fichier de base au fil des étapes.
- Étape 4 : `models/is_theia_alencon.py` et `models/res_company_alencon.py` sont fusionnés dans `models/is_theia.py` et `models/res_company.py` (code toujours au format Odoo 16).
- Seuls `__manifest__.py`, `__init__.py` et `models/__init__.py` sont nouveaux.
- Les XML d'`is_alencon` référencent encore `is_plastigray16.xxx`, et les fichiers d'`is_plastigray16` contiennent encore des parties non retenues (moules, achats, ventes…) : à traiter aux étapes suivantes.

⚠ Les tables et les champs THEIA sont écrits directement en base (`INSERT INTO`) par les Raspberry et par le programme de calcul du TRS : **ne renommer aucune table ni aucun champ**.
