---
name: diff-versions-projet
description: Compare deux snapshots et produit un diff lisible (utile à présenter au vérificateur). Déclencher sur « diff entre v1 et v2 », « qu'est-ce qui a changé ».
---

# diff-versions-projet

> 🚧 **STUB** — squelette à compléter. Owner : **Ewan**.

**Couche :** C1 · Déterministe
**Owner :** Ewan
**Statut :** `à faire`

## Objectif

Comparer deux versions du projet et lister précisément ce qui a changé.

## Entrées / Sorties

- **Entrées :** v_n, v_n-1
- **Sorties :** diff-vX-vY.md

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

Indispensable aux cycles de vérif.
