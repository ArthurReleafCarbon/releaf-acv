---
name: generer-fiche-fdes
description: Transforme le rapport d'accompagnement en fiche FDES au format INIES (transformation déterministe). Déclencher sur « générer la FDES », « produire la fiche INIES ».
---

# generer-fiche-fdes

> 🚧 **STUB** — squelette à compléter. Owner : **Nathan**.

**Couche :** C1 · Déterministe
**Owner :** Nathan
**Statut :** `à faire`

## Objectif

Produire la fiche FDES au format INIES à partir du rapport validé.

## Entrées / Sorties

- **Entrées :** rapport-accompagnement validé
- **Sorties :** fiche-fdes.xlsx

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

Template INIES figé. Référentiel INIES dans referentiels/.
