---
name: rediger-rapport-accompagnement
description: Rédige le rapport d'accompagnement (template Word verrouillé + tableaux + LLM), avec une section dédiée aux visuels produit et nom client. Déclencher sur « rédiger le rapport d'accompagnement ».
---

# rediger-rapport-accompagnement

> 🚧 **STUB** — squelette à compléter. Owner : **Nathan**.

**Couche :** C3 · Rédactionnelle (LLM + template)
**Owner :** Nathan
**Statut :** `à faire`

## Objectif

Produire une première version du rapport à partir du template, des tableaux ICV et des hypothèses.

## Entrées / Sorties

- **Entrées :** tableaux ICV, hypothèses
- **Sorties :** rapport-accompagnement.docx (V1)

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

Template à slots (placeholders tableaux + tags chiffres). Section visuels/client à prévoir.
