---
name: matcher-fe-anciennes-missions
description: Propose les FE d'une mission similaire (même produit ou famille) via une table d'affectation, pour ne pas repartir de zéro. Déclencher sur « réutiliser les FE d'une ancienne mission », « matcher les facteurs d'émission ».
---

# matcher-fe-anciennes-missions

> 🚧 **STUB** — squelette à compléter. Owner : **Arthur**.

**Couche :** C2 · Mixte (Python + LLM)
**Owner :** Arthur
**Statut :** `à faire`

## Objectif

Apprendre des rapports d'accompagnement passés pour proposer un pré-matching de FE. La sélection finale reste praticien.

## Entrées / Sorties

- **Entrées :** produit, base des missions passées
- **Sorties :** proposition de FE (à valider)

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

⚠ Attention aux FE modifiés manuellement. Critère : même produit/famille. La validation finale = praticien (dans SimaPro).
