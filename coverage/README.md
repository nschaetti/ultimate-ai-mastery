# Une couverture exhaustive, mesurable et versionnée

## État initial

[DOMAINS.md](DOMAINS.md) et [domains.json](domains.json) définissent une **matrice de planification par domaine**. Ils ne constituent pas encore un inventaire exhaustif des fonctions, classes, attributs et méthodes. Aucun taux de couverture des symboles n'est annoncé tant que le dénominateur n'a pas été établi. Une entrée `planned` ne signifie pas que le sujet est expliqué.

## Périmètre

Objectif : passer en revue toute l'API Python publique documentée de NumPy, pandas, Matplotlib, PyTorch et JAX pour les versions retenues, y compris les méthodes des classes et les sous-packages spécialisés. Les propriétés et constantes documentées font partie de la référence. Les API expérimentales et obsolètes ont des catégories distinctes. Les alias sont inventoriés avec une cible canonique, pas effacés.

Les interfaces C/C++, les extensions, les backends et les mécanismes internes ont des chapitres dédiés. Leur éventuel inventaire symbole par symbole est un périmètre distinct de celui de l'API Python. Les éléments privés non documentés ne sont pas une API stable à mémoriser. Toute exclusion doit être visible et motivée ; elle ne doit pas être comptée comme une leçon terminée.

## Construire l'inventaire

1. Installer et tester un ensemble cohérent de versions ; verrouiller les dépendances et enregistrer Python, OS, architecture et accélérateur.
2. Utiliser les index de documentation de cette version et, lorsqu'il existe, son inventaire Sphinx `objects.inv`. Archiver URL, date et empreinte du fichier source d'inventaire.
3. Filtrer les objets documentaires : un inventaire Sphinx contient aussi des titres et labels. Récupérer les membres documentés des classes et contrôler les rubriques absentes. L'introspection seule manque des API dynamiques et expose des détails privés : elle sert de complément.
4. Réconcilier symboles, alias, méthodes héritées, signatures multiples et sous-packages ; vérifier les ajouts et suppressions contre la version précédente.
5. Affecter chaque symbole à une leçon et à une fiche ; conserver les entrées non affectées dans un backlog explicite.
6. Vérifier les liens et les preuves avant de calculer une couverture.

## Format d'une future entrée de symbole

Champs requis : `library`, `version`, `symbol`, `kind`, `canonical_symbol`, `public_status`, `source_url`, `source_section`, `retrieved_at`, `lesson_id`, `reference_path`, `exercise_ids`, `explanation_status`, `exercise_status`, `solution_status`, `validation_evidence`, `exclusion_reason`.

Un champ inconnu vaut `null`, jamais une valeur inventée. Les inventaires d'une version publiée ne sont pas écrasés par les évolutions de `stable` ou `latest`.

## Statuts et indicateurs

- `planned` : contenu identifié, non rédigé.
- `draft` : contenu en cours, non validé.
- `reviewed` : contenu relu, exécution pas encore certifiée.
- `validated` : contenu relu et preuve de validation disponible.
- `deprecated` / `experimental` : propriétés de l'API, indépendantes de la maturité du contenu.

Publier séparément : symboles inventoriés, symboles expliqués, symboles exercés, corrigés validés et exclusions. Le dénominateur de couverture reste l'ensemble des symboles publics documentés dans la catégorie considérée. Afficher à part les API expérimentales, obsolètes et spécialisées. Ne jamais transformer « 100 % des lignes remplies » en « 100 % des fonctions maîtrisées ».
