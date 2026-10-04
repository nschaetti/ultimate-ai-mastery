# Parcours et prérequis

## Retour aux sources

Commencer par FND, puis NP. Alterner PD et MPL avec des données produites dans NP. Les chapitres MATH peuvent être étudiés en parallèle : vecteurs et dérivées avant l'autograd, probabilités avant les objectifs statistiques. Étudier PT et JX comme des bibliothèques à part entière, puis NN et REP.

La profondeur du parcours des bibliothèques est indépendante de l'ordre d'apprentissage : les chapitres de calcul distribué, d'extensions et de backends peuvent être repris plus tard, mais restent des éléments à couvrir.

## Branches de recherche

| Destination | Prérequis conceptuels | Progression |
|---|---|---|
| GPT et langage | NP, MATH, fondamentaux PT, NN | ATT → LM |
| Feedback et raisonnement | LM, probabilités et évaluation | RL → FB → RSN |
| Diffusion et flow matching | MATH, PT, NN ; REP utile pour les modèles latents | GEN → DIFF → FLOW |
| World models | Probabilités, REP, bases RL et séquences | WM ; DIFF/FLOW pour les variantes génératives |
| JEPA et planification latente | REP, ATT pour les encodeurs Transformer | JEPA ; WM et RL avant la planification |
| Comparer les frameworks | NP, dérivées ; bases PT et JX | Refaire MLP et entraînement avec les mêmes données, puis expliquer les divergences |

Les prérequis de chaque notebook devront être exprimés en identifiants de leçons. Ce tableau donne les dépendances entre blocs ; il n'impose pas de terminer tous les sous-packages de PyTorch avant d'étudier un Transformer.

## Mode livre de référence

Chercher le concept dans `reference/`, lire la fiche, refaire son exemple minimal sans regarder, puis ouvrir la leçon si une étape ne peut pas être expliquée. Chercher un symbole dans l'inventaire de version pour retrouver sa leçon et ses exercices. Au démarrage, ces index sont des emplacements à enrichir, pas un moteur de recherche déjà alimenté.

## Validation personnelle

À la fin d'un bloc : expliquer une idée à voix haute, la reconstruire sans le corrigé, diagnostiquer un exemple volontairement défectueux, puis transférer la méthode à un autre jeu de données. Reprendre un ancien exercice après avoir oublié son code. La vitesse ou le nombre de notebooks ouverts ne constituent pas une mesure de maîtrise.
