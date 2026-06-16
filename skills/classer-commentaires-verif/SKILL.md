---
name: classer-commentaires-verif
description: Trie les commentaires du vérificateur en 3 voies : cosmétique / data / méthodo. Déclencher sur « trier les commentaires vérificateur », « traiter la revue critique ».
---

# classer-commentaires-verif

> 🚧 **STUB** — squelette à compléter. Owner : **Vincent**.

**Couche :** C2 · Mixte (Python + LLM)
**Owner :** Vincent
**Statut :** `à faire`

## Objectif

Classer chaque commentaire pour router le bon traitement (cosmétique → narratif, data → cascade, méthodo → humain).

## Entrées / Sorties

- **Entrées :** commentaires-verif.pdf
- **Sorties :** tri commenté

## Étapes (à détailler)

1. _TODO : décrire l'algorithme / le prompt._
2. _TODO._
3. _TODO : écrire la sortie dans `v_n+1/` + log dans `_logs/`._

## Garde-fous (posture Releaf — CR 20/05)

- **L'IA exécute, elle ne propose pas d'elle-même et n'impose jamais.** La sortie est un **brouillon à contrôler** par le praticien.
- Le praticien garde la main : il challenge, valide, corrige. Le savoir-faire reste humain.
- **Pipeline idempotente** : la skill lit `projet/v_n/`, écrit dans `projet/v_n+1/` — **jamais en place**.
- Chaque exécution écrit une trace dans `_logs/` (auditabilité ISO 14025 / 14067 / EN 15804).


## Notes

Méthodo → remontée humaine, pas d'auto.
