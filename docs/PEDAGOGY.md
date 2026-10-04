# Contrat pédagogique

## Comprendre, reconstruire, retrouver

Une leçon doit permettre de répondre à quatre questions : quel problème résout-on, comment la méthode fonctionne-t-elle, comment la reconstruire, quand échoue-t-elle ? La fiche de rappel permet une relecture rapide ; le notebook contient la démonstration et les expériences. Une fiche renvoie toujours à la leçon et aux sources. « Livre de Feynman » désigne ici cette pratique personnelle de reconstruction et d'explication, sans attribution d'une méthode précise à Feynman.

## Anatomie d'une leçon

1. Identifiant stable, objectifs observables, prérequis exacts et lien vers le corrigé.
2. Versions, matériel, données, budget mesuré après exécution et limites de l'expérience.
3. Un problème concret et une prédiction à écrire avant de lancer le code.
4. Une explication intuitive et un exemple minimal entièrement résolu.
5. Une dérivation : symboles, dimensions, hypothèses, étapes intermédiaires et cas limites.
6. Des exercices gradués : reconnaître, dériver, implémenter, diagnostiquer, transférer.
7. Des tests sur des propriétés, des cas limites et une référence indépendante lorsque possible.
8. Une expérience avec baseline, variable contrôlée, visualisation et interprétation.
9. Une ablation ou un contre-exemple ; distinguer observation et explication supposée.
10. Une synthèse rédigée par l'apprenant, sans copier les formules de la leçon.
11. Une fiche de rappel et des lectures essentielles/approfondies, avec sections à lire.

## Exercices et indices

Les cellules à compléter portent le tag `exercise` et un identifiant tel que `NP-04-E02`. Utiliser `raise NotImplementedError("NP-04-E02")` pour les fonctions incomplètes, jamais une implémentation fausse silencieuse. Les cellules de vérification portent le tag `check`. Les questions ouvertes portent `reflection` et demandent une justification, pas une réponse attendue unique.

Trois indices progressifs peuvent être placés dans des blocs Markdown repliables : idée utile, démarche, pseudocode. La solution complète reste dans le fichier voisin. Les exercices doivent porter sur les mécanismes, pas sur le recopiage d'un exemple ou la mémorisation d'une signature.

Le notebook apprenant incomplet peut s'arrêter sur un exercice. Cela est attendu et ne doit pas être confondu avec un corrigé qui échoue. Ne jamais ignorer globalement les exceptions pour déclarer une exécution réussie.

## Corrigés

Conserver les mêmes identifiants et le même ordre que dans la leçon. Expliquer les choix, donner les résultats des vérifications, discuter au moins une erreur plausible et distinguer plusieurs solutions valides. Pour une expérience stochastique, fournir des plages ou tendances observées et les graines, pas une valeur arbitraire présentée comme universelle. Le corrigé doit s'exécuter depuis un kernel neuf, dans l'ordre, sans état caché.

## Référence des bibliothèques

Chaque symbole public inventorié doit avoir une explication contextualisée : rôle, signature liée à sa version, entrées/sorties, formes et dtypes, mutation ou allocation, exemple minimal, pièges et alternatives. Plusieurs variantes proches peuvent partager une leçon, mais chaque variante garde une entrée et son comportement spécifique. Les sous-packages spécialisés restent dans le parcours, même s'ils n'interviennent pas dans un GPT.

## Sources et limites

Privilégier documentation officielle, articles originaux et code des auteurs. Placer la source près de l'affirmation ou de l'équation concernée ; conserver URL, version/date, section et date de consultation. Distinguer résultat démontré, résultat expérimental des auteurs et interprétation pédagogique. Ne pas recopier des pages de documentation dans les notebooks.

Pour une méthode propriétaire, documenter les informations effectivement publiées et les inconnues. Une implémentation pédagogique doit décrire ses écarts au papier. Une prédiction vidéo n'est pas à elle seule une preuve de compréhension causale ; une chaîne de raisonnement produite n'est pas une lecture directe des calculs internes.

## Quand une leçon est-elle terminée ?

- Texte, dérivations et sources relus ; dimensions et conventions cohérentes.
- Objectifs reliés à des exercices et corrigés identifiés.
- Corrigé exécuté depuis un kernel neuf dans l'environnement verrouillé.
- Figures lisibles avec axes, unités, légendes et interprétation.
- Budget réellement mesuré et limitations matérielles indiquées.
- Fiche de rappel, navigation et couverture mises à jour.
- Statut `validated` seulement avec preuve d'exécution : environnement, commande, date et résultat.

Un statut décrit la qualité d'un contenu, pas la maîtrise de l'apprenant. Les auto-évaluations personnelles restent séparées et ne sont pas publiées automatiquement.
