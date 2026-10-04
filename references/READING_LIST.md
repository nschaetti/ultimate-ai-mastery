# Bibliographie initiale commentée

Points d'entrée consultés le **4 octobre 2026**. Cette liste amorce le cursus ; elle n'est ni exhaustive ni une certification de lecture intégrale des articles. Les futures leçons ajouteront les références précises près des affirmations, les sections à lire et les versions utilisées. Les index `stable`/`latest` évoluent : ils devront être remplacés ou accompagnés de références figées dans les inventaires.

## Bibliothèques — documentation officielle

| Source | Usage prévu | Lecture guidée |
|---|---|---|
| [NumPy reference](https://numpy.org/doc/stable/reference/index.html) | NP et inventaire de l'API | Commencer par ndarray, dtypes et ufuncs ; parcourir ensuite les routines thématiques et sous-packages. |
| [PyTorch documentation](https://docs.pytorch.org/docs/stable/index.html) | PT et implémentations des modèles | Associer API des tenseurs, autograd et modules aux exercices ; inventorier séparément les composants spécialisés. |
| [JAX API reference](https://docs.jax.dev/en/latest/jax.html) | JX et transformations fonctionnelles | Partir des arrays, transformations et pytrees ; approfondir lax, sharding, export et extensions selon le chapitre. |
| [Matplotlib API](https://matplotlib.org/stable/api/index.html) | MPL et diagnostics | Lire les interfaces objet puis les artistes et modules spécialisés ; relier chaque figure à son modèle d'objets. |
| [pandas API reference](https://pandas.pydata.org/docs/reference/index.html) | PD et préparation des données | Structurer l'inventaire autour de Series, DataFrame, Index, accessors, fenêtres, IO et extensions. |

## Articles de départ — sources primaires

| Référence | Bloc | Question de lecture |
|---|---|---|
| Vaswani et al., 2017 — [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | ATT | Comment s'articulent attention, positions, réseau feed-forward et résidus ? Refaire les dimensions du bloc. |
| Ouyang et al., 2022 — [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) | FB | Quelles données et quels objectifs distinguent SFT, reward model et optimisation de la politique ? |
| Rafailov et al., 2023 — [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) | FB | Quelles hypothèses permettent la reformulation de l'objectif de préférences ? |
| DeepSeek-AI et al., 2025 — [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | RSN | Distinguer les recettes rapportées, les évaluations des auteurs et ce que notre petite expérience pourra tester. |
| Ho et al., 2020 — [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | DIFF | Relier processus direct, processus inverse et cible de débruitage. |
| Lipman et al., 2022 — [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) | FLOW | Pourquoi peut-on apprendre un champ de vitesse à partir de chemins conditionnels ? |
| Hafner et al., 2023 — [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104) | WM | Séparer apprentissage de la dynamique, imagination et apprentissage du comportement. |
| Assran et al., 2023 — [Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2301.08243) | JEPA | Identifier les cibles prédites, le masquage et les mécanismes d'apprentissage des représentations. |

Les années ci-dessus désignent la première version arXiv, pas nécessairement l'année de publication dans une conférence ou revue. Avant une reproduction, choisir une révision précise et vérifier le code des auteurs. Les sections détaillées ne sont pas indiquées tant que le texte intégral correspondant n'a pas été étudié.

## Lectures à compléter

Les bibliographies propres à l'autograd, au contraste, à la distillation, aux variantes d'attention, au RL, aux VAE, au score matching, aux rectified flows, aux world models vidéo et aux variantes vidéo/action de JEPA seront établies lors de la rédaction des chapitres. Ne pas interpréter leur absence ici comme une exclusion du programme.
