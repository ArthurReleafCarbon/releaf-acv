---
name: post-traiter-export-simapro
description: Transforme l'export SimaPro brut en tableaux ICV consolidés prêts pour le rapport. Déclencher sur « post-traiter l'export », « générer les tableaux ICV ».
---

# post-traiter-export-simapro

> 🚧 **STUB** — squelette à compléter. Owner : **Arthur**.

**Couche :** C1 · Déterministe
**Owner :** Arthur
**Statut :** `à faire`

## Objectif

Consolider l'export SimaPro en 10+ tableaux ICV normalisés, sans recopie manuelle.

## Entrées / Sorties

- **Entrées :** export-simapro.xlsx
- **Sorties :** tableaux-icv.xlsx

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

Alimente rediger-rapport-accompagnement.
