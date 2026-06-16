---
name: rediger-fiche-fdes-narrative
description: Rédige les parties narratives de la FDES. Déclencher sur « rédiger la narrative FDES ».
---

# rediger-fiche-fdes-narrative

> 🚧 **STUB** — squelette à compléter. Owner : **Nathan**.

**Couche :** C3 · Rédactionnelle (LLM + template)
**Owner :** Nathan
**Statut :** `à faire`

## Objectif

Compléter les zones narratives de la fiche FDES.

## Entrées / Sorties

- **Entrées :** fiche FDES
- **Sorties :** parties narratives rédigées

## Étapes (à détailler)

1. _TODO : décrire l'algorithme / le prompt._
2. _TODO._
3. _TODO : écrire la sortie dans `v_n+1/` + log dans `_logs/`._

## Garde-fous (posture Releaf — CR 20/05)

- **L'IA exécute, elle ne propose pas d'elle-même et n'impose jamais.** La sortie est un **brouillon à contrôler** par le praticien.
- Le praticien garde la main : il challenge, valide, corrige. Le savoir-faire reste humain.
- **Pipeline idempotente** : la skill lit `projet/v_n/`, écrit dans `projet/v_n+1/` — **jamais en place**.
- Chaque exécution écrit une trace dans `_logs/` (auditabilité ISO 14025 / 14067 / EN 15804).

