---
name: expliquer-commentaires-verif
description: Se met à la place de l'auditeur et explique un commentaire ambigu (« ce commentaire signifie probablement… »). Déclencher sur « explique-moi ce commentaire du vérificateur », « qu'est-ce qu'il veut dire ».
---

# expliquer-commentaires-verif

> 🚧 **STUB** — squelette à compléter. Owner : **Vincent**.

**Couche :** C2 · Mixte (Python + LLM)
**Owner :** Vincent
**Statut :** `à faire`

## Objectif

Aider le praticien à comprendre un commentaire peu clair en reformulant l'intention probable de l'auditeur.

## Entrées / Sorties

- **Entrées :** commentaire isolé (+ contexte rapport)
- **Sorties :** explication / reformulation

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

Nourrie par INIES + norme. Reste une suggestion.
