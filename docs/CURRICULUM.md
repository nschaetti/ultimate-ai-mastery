# Sommaire détaillé

Tous les éléments ci-dessous sont **prévus**, pas encore rédigés. Chaque ligne correspond à une unité pédagogique pouvant nécessiter plusieurs notebooks. Les identifiants sont stables ; ils serviront aux prérequis, exercices, fiches et inventaires. Les chapitres spécialisés restent dans le périmètre même si leur réalisation vient plus tard.

Les cinq blocs de bibliothèques constituent des parcours autonomes et approfondis. Ce sommaire organise la matière ; seul un inventaire public versionné permettra de démontrer une couverture exhaustive des API.

## FND — Pratique scientifique et Python

**Prérequis du bloc :** Aucun ; diagnostic initial.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| FND-01 | Environnement et notebooks | Repartir d'un kernel neuf, identifier les dépendances et reconnaître un état caché. |
| FND-02 | Python scientifique | Maîtriser itérateurs, générateurs, context managers, fonctions, classes et protocoles utiles aux bibliothèques. |
| FND-03 | Tests numériques | Comparer exactitude, tolérances, invariants et tests fondés sur des propriétés. |
| FND-04 | Reproductibilité | Distinguer graine, déterminisme et variabilité statistique. |
| FND-05 | Mesure et débogage | Mesurer temps et mémoire sans confondre compilation, transfert et calcul. |
| FND-06 | Lire un article | Extraire hypothèses, objectif, protocole et écarts entre article et code. |

## NP — NumPy — maîtrise de la bibliothèque

**Prérequis du bloc :** FND ; MATH selon les domaines.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| NP-01 | Le modèle ndarray | Expliquer shape, ndim, size, axes, dtype et représentation en mémoire. |
| NP-02 | Création et conversions | Choisir les constructeurs, conversions et routines de création selon les garanties requises. |
| NP-03 | Types et promotion | Prédire promotion, casting, overflow et précision des calculs. |
| NP-04 | Indexation et sélection | Comparer slicing, indexation avancée, masques, take et mises à jour. |
| NP-05 | Vues, copies et strides | Prédire le partage mémoire, la contiguïté et le coût d'une transformation. |
| NP-06 | Broadcasting et formes | Dériver les formes compatibles et détecter un résultat plausible mais incorrect. |
| NP-07 | Ufuncs et réductions | Utiliser out, where, axes, reduce, accumulate et la gestion des erreurs flottantes. |
| NP-08 | Assemblage et organisation | Comparer reshape, transpose, stacking, splitting, répétition et padding. |
| NP-09 | Mathématiques, logique et ensembles | Choisir les opérations élémentaires, complexes, bitwise, logiques et ensemblistes. |
| NP-10 | Tri, recherche et statistiques | Analyser axes, stabilité, quantiles, histogrammes, NaN et conventions statistiques. |
| NP-11 | Algèbre linéaire et contractions | Relier solve, décompositions, normes, matmul, tensordot et einsum aux équations. |
| NP-12 | Génération aléatoire | Utiliser Generator, BitGenerator, distributions et flux indépendants reproductibles. |
| NP-13 | Fourier et fenêtres | Relier spectres, fréquences, normalisation, symétries et fenêtrage. |
| NP-14 | Polynômes et ajustement | Comparer bases polynomiales, évaluation, dérivation, ajustement et conditionnement. |
| NP-15 | Chaînes, dates et tableaux structurés | Manipuler données non purement flottantes et comprendre leurs limites. |
| NP-16 | Tableaux masqués et domaines étendus | Comparer masques, valeurs manquantes et fonctions à domaine complexe. |
| NP-17 | Entrées-sorties et memmap | Choisir les formats, charger partiellement et expliquer persistance et représentation. |
| NP-18 | Typing, testing et configuration | Exploiter annotations, assertions numériques, options et diagnostics. |
| NP-19 | Interopérabilité et extensions | Étudier protocoles array, DLPack, F2PY, panorama C-API et compatibilité Array API. |
| NP-20 | Audit des API spécialisées | Réconcilier toutes les rubriques et symboles publics de la version avec leurs leçons. |

## PD — pandas — maîtrise de la bibliothèque

**Prérequis du bloc :** NP : tableaux, types et indexation.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| PD-01 | Series, DataFrame et Index | Expliquer axes nommés, alignement et différence avec un ndarray. |
| PD-02 | Construction, types et conversion | Choisir types nullable, catégoriels et types d'extension. |
| PD-03 | Indexation et mutation | Maîtriser loc, iloc, filtres, alignement et sémantique de copie de la version. |
| PD-04 | Valeurs manquantes | Comparer sentinelles, propagation, détection et stratégies d'imputation. |
| PD-05 | Calcul et statistiques | Distinguer opérations vectorisées, apply, agrégation et alignement implicite. |
| PD-06 | GroupBy | Construire split-apply-combine, transform, filter et agrégations multiples. |
| PD-07 | Jointures et concaténation | Détecter cardinalité inattendue, clés manquantes et duplication de lignes. |
| PD-08 | Reshape et MultiIndex | Passer entre formats longs/larges avec pivot, melt, stack et unstack. |
| PD-09 | Texte et catégories | Utiliser accessors str et cat, expressions régulières et catégories ordonnées. |
| PD-10 | Temps et fuseaux horaires | Distinguer Timestamp, Timedelta, Period, resampling et localisation. |
| PD-11 | Fenêtres | Comparer rolling, expanding et pondération exponentielle. |
| PD-12 | Entrées-sorties | Passer en revue les interfaces de lecture/écriture et leurs dépendances optionnelles. |
| PD-13 | Visualisation et Styler | Séparer analyse graphique, formatage et export de tableaux. |
| PD-14 | Performance et mémoire | Mesurer coût des types, de l'index et des opérations sur gros tableaux. |
| PD-15 | Extensions, options et testing | Comprendre ExtensionArray, options, objets sparse et assertions pandas. |
| PD-16 | Audit des API et migrations | Inventorier méthodes, accessors, attributs et changements de version. |

## MPL — Matplotlib — maîtrise de la bibliothèque

**Prérequis du bloc :** NP : tableaux ; statistiques élémentaires.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| MPL-01 | Figure, Axes, Axis et Artist | Construire un tracé avec l'API objet et expliquer le rôle de pyplot. |
| MPL-02 | Courbes, marqueurs et erreurs | Choisir Line2D, styles, barres d'erreur et représentations d'incertitude. |
| MPL-03 | Graphiques statistiques | Comparer histogrammes, barres, scatter, boxplots et violons. |
| MPL-04 | Images, grilles et contours | Choisir imshow, pcolormesh, contour et interpolation selon les données. |
| MPL-05 | Couleurs et normalisation | Relier colormaps, normes, colorbars et perception des valeurs. |
| MPL-06 | Axes, échelles et ticks | Contrôler limites, échelles, locators, formatters, unités et dates. |
| MPL-07 | Texte et annotations | Configurer polices, mathtext, légendes, annotations et export typographique. |
| MPL-08 | Disposition des figures | Maîtriser subplots, mosaïques, GridSpec et moteurs de layout. |
| MPL-09 | Transformations et géométrie | Passer entre coordonnées données, axes et figure ; utiliser paths et patches. |
| MPL-10 | Collections et tracés spécialisés | Expliquer collections, graphes triangulés, vecteurs et projections. |
| MPL-11 | Styles et configuration | Construire un style reproductible avec rcParams et contextes locaux. |
| MPL-12 | Animation et événements | Mettre à jour les artistes, gérer événements, widgets et export d'animations. |
| MPL-13 | Backends et export | Distinguer interactif, raster et vectoriel ; choisir DPI et formats. |
| MPL-14 | Toolkits | Explorer mplot3d, axes_grid1 et axisartist avec leurs limites. |
| MPL-15 | API de bas niveau et audit | Cartographier modules spécialisés, transformations, rendu et API publiques restantes. |

## MATH — Mathématiques pour reconstruire les modèles

**Prérequis du bloc :** NP en parallèle.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| MATH-01 | Vecteurs, matrices et espaces | Relier bases, projections, rang et changements de coordonnées. |
| MATH-02 | Décompositions et conditionnement | Interpréter valeurs propres, SVD et stabilité d'une résolution. |
| MATH-03 | Calcul différentiel | Dériver gradients, Jacobiennes, Hessiennes et règle de chaîne avec dimensions. |
| MATH-04 | Probabilités | Manipuler conditionnement, indépendance, Bayes et marginalisation. |
| MATH-05 | Estimation et Monte Carlo | Comparer biais, variance, intervalles et approximation d'espérances. |
| MATH-06 | Information et vraisemblance | Dériver log-vraisemblance, entropie, cross-entropy et KL. |
| MATH-07 | Optimisation | Comparer SGD, momentum, méthodes adaptatives et contraintes. |
| MATH-08 | Calcul variationnel élémentaire | Dériver un ELBO et distinguer approximation et objectif exact. |
| MATH-09 | ODE, SDE et transport | Relier champs de vecteurs, intégration numérique et évolution de densités. |

## PT — PyTorch — maîtrise de la bibliothèque

**Prérequis du bloc :** NP ; MATH : dérivées pour autograd.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| PT-01 | Tenseurs et dispositifs | Maîtriser création, types, devices, conversions et partage mémoire. |
| PT-02 | Indexation et opérations | Passer en revue opérations Tensor, broadcasting, réductions et mutation. |
| PT-03 | Autograd | Expliquer graphe, leaf tensors, accumulation, detach et contextes de gradient. |
| PT-04 | Dérivées avancées | Construire JVP, VJP, Hessiennes et opérations différentiables personnalisées. |
| PT-05 | Modules et paramètres | Comprendre nn.Module, buffers, paramètres, hooks et state_dict. |
| PT-06 | Couches et fonctionnelles | Cartographier nn et nn.functional, initialisations, activations et losses. |
| PT-07 | Optimiseurs et schedules | Examiner états, groupes de paramètres, zero_grad et scheduling. |
| PT-08 | Données et parallélisme de chargement | Maîtriser Dataset, IterableDataset, DataLoader, collate et workers. |
| PT-09 | Aléatoire et distributions | Comparer échantillonnage, reparamétrisation, RNG et déterminisme. |
| PT-10 | Algèbre, FFT et formats spécialisés | Explorer linalg, fft, sparse, tenseurs quantifiés et nested selon la version. |
| PT-11 | Précision et mémoire | Mesurer AMP, checkpointing, transferts et consommation des tenseurs. |
| PT-12 | Programmation fonctionnelle | Utiliser torch.func pour gradients par exemple et transformations vectorisées. |
| PT-13 | Compilation et export | Étudier compile, export, ruptures de graphe, formes dynamiques et outils historiques. |
| PT-14 | Profilage et benchmark | Localiser un goulot sans confondre exécution asynchrone et temps mesuré. |
| PT-15 | Calcul distribué | Comprendre collectives, DDP, sharding et sauvegarde distribuée. |
| PT-16 | Sérialisation et déploiement | Gérer checkpoints, chargement, interopérabilité et formats d'export. |
| PT-17 | Backends et extensions | Explorer accélérateurs, bibliothèques d'opérateurs et extensions C++/CUDA. |
| PT-18 | Testing et audit des modules | Réconcilier testing, utils et toutes les API publiques restantes avec l'inventaire. |

## JX — JAX — maîtrise de la bibliothèque

**Prérequis du bloc :** NP ; MATH : dérivées.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| JX-01 | Arrays et jax.numpy | Comparer sémantique, types, devices, immutabilité et mises à jour fonctionnelles. |
| JX-02 | Pytrees et état | Représenter paramètres et état sans mutations cachées. |
| JX-03 | Aléatoire explicite | Gérer clés, split, distributions et indépendance des tirages. |
| JX-04 | Différentiation | Comparer grad, value_and_grad, jacfwd, jacrev, jvp et vjp. |
| JX-05 | Compilation et tracing | Expliquer jit, valeurs statiques, spécialisation et recompilation. |
| JX-06 | Vectorisation | Dériver in_axes/out_axes et composer vmap avec jit et grad. |
| JX-07 | Contrôle de flux et lax | Utiliser cond, scan, boucles et primitives adaptées au tracing. |
| JX-08 | Règles de dérivation personnalisées | Écrire custom_jvp/custom_vjp et vérifier leurs hypothèses. |
| JX-09 | Réseaux, images et fonctions scientifiques | Explorer jax.nn, initializers, jax.image et jax.scipy. |
| JX-10 | Placement et sharding | Comprendre maillages, partitionnement et calcul multi-dispositifs. |
| JX-11 | Mémoire et précision | Étudier donation, remat, offloading, X64 et tolérances. |
| JX-12 | Débogage et profilage | Inspecter valeurs d'exécution, erreurs transformées et synchronisation des benchmarks. |
| JX-13 | Export, stages et interopérabilité | Étudier compilation anticipée, export, DLPack, callbacks et FFI. |
| JX-14 | API expérimentales et kernels | Cartographier experimental, sparse et Pallas selon la version. |
| JX-15 | Extensions et représentation interne | Lire un jaxpr et situer jax.extend sans confondre API publique et interne. |
| JX-16 | Audit des modules | Réconcilier l'ensemble des symboles documentés et leurs changements de version. |

## NN — Réseaux de neurones

**Prérequis du bloc :** MATH ; fondamentaux PT ou JX.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| NN-01 | Régression linéaire et logistique | Dériver objectifs et gradients puis comparer à une solution analytique. |
| NN-02 | Autograd miniature | Implémenter un moteur scalaire puis relier ses limites aux tenseurs. |
| NN-03 | MLP et backpropagation | Reconstruire la propagation avant et arrière avec dimensions explicites. |
| NN-04 | Initialisation et activations | Mesurer propagation de variance et saturation. |
| NN-05 | Normalisation et régularisation | Comparer batch/layer normalization, dropout et pénalités. |
| NN-06 | Optimisation et diagnostic | Surapprendre un minibatch puis diagnostiquer gradients et courbes. |
| NN-07 | Convolutions | Dériver padding, stride, réceptivité et partage des poids. |
| NN-08 | Récurrence et mémoire | Comparer RNN, LSTM et GRU sur une tâche de dépendance temporelle. |
| NN-09 | Généralisation et calibration | Évaluer hors échantillon, séparation des données et confiance. |

## REP — Représentations et auto-supervision

**Prérequis du bloc :** NN ; probabilités.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| REP-01 | Autoencodeurs | Distinguer reconstruction, compression et utilité des représentations. |
| REP-02 | Contraste | Implémenter une perte contrastive et étudier température et négatifs. |
| REP-03 | Distillation et enseignants | Comparer stop-gradient, cibles mobiles et apprentissage enseignant-élève. |
| REP-04 | Effondrement | Construire une solution dégénérée et tester des contraintes anti-effondrement. |
| REP-05 | Prédiction masquée | Comparer prédiction dans l'espace des entrées et des représentations. |
| REP-06 | Évaluation des représentations | Distinguer linear probe, fine-tuning, transfert et fuite d'information. |

## ATT — Attention et Transformers

**Prérequis du bloc :** NN ; NP : contractions.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| ATT-01 | Attention additive | Construire requêtes, clés, valeurs et scores d'alignement. |
| ATT-02 | Scaled dot-product | Dériver scaling, softmax, masques et gradients. |
| ATT-03 | Multi-head et cross-attention | Tracer toutes les dimensions et tester le mélange des têtes. |
| ATT-04 | Positions | Comparer positions absolues, relatives, RoPE et biais positionnels. |
| ATT-05 | Bloc Transformer | Comparer résidus, pre/post-norm et réseaux feed-forward. |
| ATT-06 | MQA et GQA | Quantifier partage des clés/valeurs et taille du cache. |
| ATT-07 | Attention locale et sparse | Construire motifs de connexion et analyser leur effet sur l'information. |
| ATT-08 | Attention linéaire | Comprendre factorisations, approximations et différences avec le softmax dense. |
| ATT-09 | Attention efficace exacte | Expliquer tiling, softmax en ligne et principes de FlashAttention. |
| ATT-10 | Alternatives séquentielles | Comparer récurrence, modèles d'état et architectures hybrides à budget contrôlé. |

## LM — GPT et modèles de langage

**Prérequis du bloc :** ATT ; estimation statistique.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| LM-01 | Tokenisation | Implémenter un tokenizer simple et analyser segmentation et vocabulaire. |
| LM-02 | Corpus et préparation | Documenter provenance, déduplication, découpage et contamination. |
| LM-03 | GPT minimal | Assembler un modèle decoder-only causal et vérifier l'absence de fuite future. |
| LM-04 | Préentraînement | Relier next-token prediction, batching, loss et budget de calcul. |
| LM-05 | Échantillonnage | Comparer température, top-k et top-p sur distributions contrôlées. |
| LM-06 | Cache et inférence | Vérifier égalité des logits avec/sans KV cache et mesurer le compromis mémoire. |
| LM-07 | Architectures et efficacité | Étudier normalisations, activations, MoE et adaptations paramétriquement efficaces. |
| LM-08 | Évaluation | Comparer perplexité, tâches aval, robustesse et limites des benchmarks. |
| LM-09 | Multimodalité | Relier encodeurs, projections et séquences mixtes sur un exemple réduit. |

## RL — Bases du renforcement

**Prérequis du bloc :** MATH : probabilités ; NN.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| RL-01 | MDP et observabilité partielle | Distinguer état, observation, action, récompense et croyance. |
| RL-02 | Valeurs et Bellman | Résoudre un petit problème tabulaire et vérifier les équations. |
| RL-03 | Policy gradient | Dériver REINFORCE, baseline et variance. |
| RL-04 | Actor-critic et PPO | Comprendre avantages, clipping, contraintes et données on-policy. |
| RL-05 | Hors politique et évaluation | Analyser décalage de distribution et limites des estimations. |
| RL-06 | Planification | Comparer recherche, MPC et politique apprise sur un même environnement. |

## FB — Feedback et post-entraînement

**Prérequis du bloc :** LM ; RL pour les méthodes par renforcement.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| FB-01 | Instruction tuning | Construire exemples supervisés, masques de loss et protocole d'évaluation. |
| FB-02 | Préférences | Modéliser comparaisons, désaccords et biais des annotateurs. |
| FB-03 | Reward models | Entraîner un score de préférence et analyser calibration et extrapolation. |
| FB-04 | RLHF | Relier politique, modèle de référence, récompense et pénalisation KL. |
| FB-05 | DPO | Dériver l'objectif et expliciter hypothèses et données nécessaires. |
| FB-06 | Feedback automatique | Comparer règles vérifiables, juges modèles et supervision humaine. |
| FB-07 | Reward hacking | Construire un exemple d'optimisation d'un proxy qui dégrade l'objectif réel. |
| FB-08 | Évaluation du post-entraînement | Séparer qualité, style, longueur, préférences et robustesse. |

## RSN — Modèles de raisonnement

**Prérequis du bloc :** LM, FB et RL.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| RSN-01 | Tâches et protocoles | Construire tâches vérifiables et splits empêchant la mémorisation triviale. |
| RSN-02 | Traces de raisonnement | Comparer réponse directe et étapes explicites sans assimiler texte et mécanisme interne. |
| RSN-03 | Vérification | Comparer supervision du résultat et des étapes, erreurs et coût d'annotation. |
| RSN-04 | Calcul à l'inférence | Comparer best-of-N, vote et recherche à budget de tokens égal. |
| RSN-05 | Renforcement à récompense vérifiable | Implémenter une expérience limitée et analyser avantages et normalisations de type GRPO. |
| RSN-06 | Distillation | Transférer des solutions tout en contrôlant qualité et contamination. |
| RSN-07 | Généralisation | Mesurer longueur, difficulté, robustesse et transfert hors distribution. |
| RSN-08 | Reproduction critique | Distinguer recette publiée, résultat reproduit et informations indisponibles. |

## GEN — Modèles génératifs et variables latentes

**Prérequis du bloc :** MATH, NN.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| GEN-01 | Densités et échantillonnage | Distinguer estimation de densité, génération et qualité perceptuelle. |
| GEN-02 | VAE | Dériver ELBO, reparamétrisation et rôle du prior. |
| GEN-03 | Normalizing flows | Implémenter changement de variables, couplages et log-déterminants. |
| GEN-04 | GAN et objectifs adversariaux | Comprendre le jeu d'optimisation et diagnostiquer l'effondrement de modes. |
| GEN-05 | Score matching | Relier gradients de log-densité et objectifs de débruitage. |
| GEN-06 | Évaluation générative | Comparer couverture, fidélité, métriques et biais d'évaluation. |

## DIFF — Diffusion

**Prérequis du bloc :** GEN ; ODE/SDE pour les approfondissements.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| DIFF-01 | Processus direct | Dériver bruitage, marginales et schedules. |
| DIFF-02 | Processus inverse | Relier débruitage, objectif d'entraînement et paramètres prédits. |
| DIFF-03 | DDPM miniature | Apprendre une distribution 2D et visualiser les étapes inverses. |
| DIFF-04 | DDIM et solveurs | Comparer nombre d'étapes, stochasticité et erreur numérique. |
| DIFF-05 | Score et SDE | Relier formulations discrètes, score et dynamique continue. |
| DIFF-06 | Conditionnement et guidance | Comparer guidage par classifieur et classifier-free guidance. |
| DIFF-07 | Diffusion latente | Analyser le rôle de l'autoencodeur et la perte d'information. |
| DIFF-08 | U-Net et DiT | Comparer architectures de débruitage à protocole contrôlé. |

## FLOW — Flow matching et transport

**Prérequis du bloc :** GEN ; MATH : ODE.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| FLOW-01 | Transport continu | Dériver la relation entre trajectoires, vitesse et densités. |
| FLOW-02 | Chemins conditionnels | Construire interpolation, bruit et cibles de vitesse. |
| FLOW-03 | Conditional flow matching | Dériver puis implémenter l'objectif sur une distribution 2D. |
| FLOW-04 | Couplages | Comparer couplage indépendant et couplages orientés transport. |
| FLOW-05 | Rectified flows | Étudier rectification, trajectoires et coût numérique. |
| FLOW-06 | Intégration et génération | Mesurer qualité et coût selon solveur et nombre d'évaluations. |
| FLOW-07 | Comparaison avec diffusion | Expliciter paramétrisations communes et différences d'objectifs. |
| FLOW-08 | Conditionnement et distillation | Tester guidage et réduction du coût de génération. |

## WM — World models — familles et usages

**Prérequis du bloc :** REP, RL ; séquences ; DIFF/FLOW pour les variantes.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| WM-01 | Définir le monde modélisé | Distinguer prédiction d'observations, dynamique d'état et modèle pour le contrôle. |
| WM-02 | Dynamique déterministe | Apprendre transitions et analyser les erreurs multi-pas. |
| WM-03 | Dynamique probabiliste | Représenter ambiguïté, variables latentes et incertitude. |
| WM-04 | Modèles récurrents latents | Reconstruire un RSSM miniature et ses objectifs. |
| WM-05 | Imagination et contrôle | Comparer planification dans le modèle et politique entraînée dans l'imagination. |
| WM-06 | World models à tokens | Étudier quantification, séquences et accumulation des erreurs. |
| WM-07 | Modèles vidéo génératifs | Comparer autorégression, diffusion et flow matching pour la prédiction temporelle. |
| WM-08 | Actions et contrôlabilité | Tester l'effet d'actions et interventions plutôt que la seule qualité visuelle. |
| WM-09 | Incertitude et distribution | Mesurer dérive, calibration et échec hors distribution. |
| WM-10 | Évaluation comparative | Comparer pixel, état latent, prédiction de récompense et performance de contrôle. |

## JEPA — JEPA et prédiction latente

**Prérequis du bloc :** REP ; ATT selon l'encodeur ; WM/RL pour le contrôle.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| JEPA-01 | Architecture prédictive | Définir encodeur contexte, encodeur cible, prédicteur et objectif. |
| JEPA-02 | Masquage et cible | Étudier difficulté de prédiction, stop-gradient et mise à jour de l'enseignant. |
| JEPA-03 | Anti-effondrement | Analyser ce qui évite ou non une représentation constante. |
| JEPA-04 | JEPA image | Construire une expérience miniature et expliciter les écarts à I-JEPA. |
| JEPA-05 | JEPA vidéo | Étudier temporalité, cibles et évaluation des représentations. |
| JEPA-06 | Actions et planification latente | Formuler les composants supplémentaires nécessaires au contrôle. |
| JEPA-07 | Comparaison contrôlée | Comparer reconstruction, contraste et prédiction latente à encodeur et données fixés. |
| JEPA-08 | Limites et recherche | Tester invariances utiles, information perdue et généralisation. |

## PRJ — Projets de synthèse

**Prérequis du bloc :** Prérequis propres à chaque branche.

| Unité | Chapitre / sous-chapitre | Objectif observable |
|---|---|---|
| PRJ-01 | Bibliothèques sans béquilles | Résoudre un problème numérique et produire un rapport graphique sans copier une solution. |
| PRJ-02 | GPT de bout en bout | Livrer corpus documenté, modèle, entraînement, génération et protocole d'évaluation. |
| PRJ-03 | Raisonnement vérifiable | Comparer SFT, sélection et une méthode RL avec contrôle des budgets. |
| PRJ-04 | Diffusion contre flow matching | Comparer les deux sur mêmes données, capacités et budget d'évaluation. |
| PRJ-05 | World model pour le contrôle | Comparer modèle appris, modèle oracle et baseline sans modèle. |
| PRJ-06 | JEPA contre reconstruction | Comparer représentations et performance aval avec ablations. |
| PRJ-07 | Reproduire un papier | Établir un plan de reproduction, journaliser les écarts et publier résultats négatifs compris. |
