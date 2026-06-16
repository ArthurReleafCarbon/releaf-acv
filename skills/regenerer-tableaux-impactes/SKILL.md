---
name: regenerer-tableaux-impactes
description: Régénère uniquement les tableaux touchés par un changement (pas tous). Déclencher sur « régénérer les tableaux impactés ».
---

# regenerer-tableaux-impactes

> 🚧 **STUB** — squelette à compléter. Owner : **Ewan**.

**Couche :** C1 · Déterministe
**Owner :** Ewan
**Statut :** `à faire`

## Objectif

Recalculer seulement les tableaux affectés par un changement, laisser les autres intacts.

## Entrées / Sorties

- **Entrées :** diff données
- **Sorties :** tableaux mis à jour (uniquement les impactés)

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

Cœur du gain de temps en cycle vérif.
