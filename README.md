# Ultimate AI Mastery

Un retour aux sources pour reconstruire une maîtrise profonde de l'intelligence artificielle : calcul scientifique, bibliothèques, réseaux neuronaux, modèles de langage, raisonnement, diffusion, flow matching et world models.

Ce dépôt a deux usages : **un cursus de notebooks guidés** et **un livre personnel auquel revenir pour retrouver une idée, la dériver et la réimplémenter**. Le niveau visé est master avancé/recherche ; les fondations sont reconstruites sans supposer qu'elles sont encore fraîches.

## Entrer dans le livre

| Besoin | Entrée |
|---|---|
| Voir tous les chapitres et leurs objectifs | [Sommaire détaillé](docs/CURRICULUM.md) |
| Choisir un parcours et comprendre les prérequis | [Guide de lecture](docs/LEARNING_PATHS.md) |
| Réviser une notion ou une API | [Index du livre de référence](reference/README.md) |
| Vérifier ce que « tout couvrir » signifie | [Politique de couverture](coverage/README.md) et [matrice des domaines](coverage/DOMAINS.md) |
| Comprendre la forme des exercices et corrigés | [Contrat pédagogique](docs/PEDAGOGY.md) |
| Retrouver les sources de départ | [Bibliographie commentée](references/READING_LIST.md) |
| Voir le prochain travail concret | [Feuille de route](docs/ROADMAP.md) |

## État réel du dépôt

Cette première version établit le plan, les conventions, la matrice des domaines et les gabarits. **Les chapitres du cursus ne sont pas encore rédigés.** Les gabarits ne sont pas des leçons terminées. L'inventaire exhaustif des symboles des bibliothèques et les environnements verrouillés restent à construire et à vérifier.

Les bibliothèques ont leur propre parcours approfondi : **NumPy, pandas, Matplotlib, PyTorch et JAX**. Leur couverture ne se limite pas aux fonctions employées dans les projets d'IA. SciPy, les outils de tokenisation et les écosystèmes associés seront ajoutés explicitement au périmètre quand un chapitre les nécessite.

## Organisation

- `notebooks/` : chapitres ; chaque leçon aura `lesson.ipynb` et `solution.ipynb` côte à côte.
- `reference/` : fiches de rappel, index des concepts et index des API.
- `coverage/` : couverture des domaines, puis des symboles publics par version.
- `references/` : lectures et provenance des explications.
- `templates/` : gabarits de leçon, corrigé et fiche de rappel.
- `docs/` : progression, prérequis, règles pédagogiques et feuille de route.
- `environments/` : politique des environnements reproductibles.

Les explications sont en français ; les noms d'API, le code, les commentaires et les docstrings restent en anglais. Les expériences privilégient des données synthétiques et des tailles raisonnables, puis proposent des approfondissements. Aucune performance de grand modèle n'est promise à partir d'une reproduction miniature.
