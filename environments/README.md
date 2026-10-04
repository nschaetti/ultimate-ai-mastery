# Environnements reproductibles

Statut : à établir. Aucun ensemble de versions n'a encore été installé et validé pour le cursus. Les liens `stable` et `latest` de la bibliographie sont des points d'entrée, pas des verrous de dépendances.

Prévoir un environnement calcul scientifique/NumPy/pandas/Matplotlib, un environnement PyTorch et un environnement JAX, avec un noyau Jupyter identifiable pour chacun. Cela permet de gérer leurs contraintes d'accélération indépendamment. Ne pas installer ou modifier les pilotes du système depuis un notebook.

Avant le premier chapitre validé, créer les fichiers de dépendances et leurs verrous exacts ; tester les imports et une opération représentative sur CPU. Ajouter des profils GPU seulement après vérification sur le matériel cible. Les chapitres devront enregistrer les versions effectivement exécutées, et non la version supposée la plus récente.

Pour chaque expérience : graine, provenance/licence des données, commande d'exécution, versions, matériel, durée observée et mémoire maximale si mesurée. La reproductibilité numérique exacte peut varier selon matériel, backend et opérations ; documenter les tolérances. Les jeux de données volumineux et poids restent hors Git. Leur téléchargement sera explicite.
