---
name: convertir-unites
description: Convertit les unités des données de collecte vers l'unité fonctionnelle (UF) via les ratios de conversion embarqués. Déclencher sur « convertir les unités », « ramener à l'UF ».
---

# convertir-unites

> 🚧 **STUB** — squelette à compléter. Owner : **Ewan**.

**Couche :** C1 · Déterministe
**Owner :** Ewan
**Statut :** `à faire`

## Objectif

Appliquer les ratios de conversion (référentiel embarqué) pour ramener toutes les données à l'UF.

## Entrées / Sorties

- **Entrées :** fichier collecte, UF cible
- **Sorties :** valeurs converties + journal des conversions

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

Ratios dans referentiels/ratios-conversion.md. Toute conversion est tracée.
