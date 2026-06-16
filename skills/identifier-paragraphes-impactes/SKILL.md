---
name: identifier-paragraphes-impactes
description: Repère quels paragraphes du rapport doivent être mis à jour suite à un changement de chiffres. Déclencher sur « quels paragraphes sont impactés ».
---

# identifier-paragraphes-impactes

> 🚧 **STUB** — squelette à compléter. Owner : **Nathan**.

**Couche :** C2 · Mixte (Python + LLM)
**Owner :** Nathan
**Statut :** `à faire`

## Objectif

Lister les paragraphes liés aux tableaux/chiffres qui ont bougé.

## Entrées / Sorties

- **Entrées :** rapport, diff
- **Sorties :** liste des paragraphes à toucher

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

Alimente mettre-a-jour-narratif-cible.
