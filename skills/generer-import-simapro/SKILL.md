---
name: generer-import-simapro
description: Génère le fichier Excel d'import SimaPro depuis la trame validée (reverse engineering du format officiel d'import). PRIORITÉ N°1. Déclencher sur « générer l'import SimaPro », « préparer le fichier d'import ».
---

# generer-import-simapro

> 🚧 **STUB** — squelette à compléter. Owner : **Arthur**.

**Couche :** C1 · Déterministe
**Owner :** Arthur
**Statut :** `à faire`

## Objectif

Transformer la trame de collecte validée en fichier Excel chargeable directement dans SimaPro (remplace +1000 saisies manuelles).

## Entrées / Sorties

- **Entrées :** trame-collecte validée
- **Sorties :** import-simapro.xlsx

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

Cœur du pain point n°1. Mapping trame → import à documenter dans references/.
