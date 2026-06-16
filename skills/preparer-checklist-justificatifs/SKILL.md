---
name: preparer-checklist-justificatifs
description: Génère la checklist des justificatifs à demander au client selon le scénario. Déclencher sur « préparer la checklist client », « quels justificatifs demander ».
---

# preparer-checklist-justificatifs

> 🚧 **STUB** — squelette à compléter. Owner : **Guillaume**.

**Couche :** C2 · Mixte (Python + LLM)
**Owner :** Guillaume
**Statut :** `à faire`

## Objectif

Produire la liste des pièces justificatives à collecter côté client selon le scénario.

## Entrées / Sorties

- **Entrées :** scénario projet
- **Sorties :** checklist-client.md

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

Orienté relation client.
