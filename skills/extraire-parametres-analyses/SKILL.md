---
name: extraire-parametres-analyses
description: Prépare les paramètres à copier-coller dans SimaPro pour les analyses de sensibilité/variabilité/gravité. NE FAIT PAS les analyses (= 100% humain). Déclencher sur « préparer les paramètres d'analyse ».
---

# extraire-parametres-analyses

> 🚧 **STUB** — squelette à compléter. Owner : **Nathan**.

**Couche :** C1 · Déterministe
**Owner :** Nathan
**Statut :** `à faire`

## Objectif

Extraire et formater les paramètres pour que le praticien relance les analyses dans SimaPro (version premium ++).

## Entrées / Sorties

- **Entrées :** tableaux ICV
- **Sorties :** parametres-analyses.md

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

⚠ Les analyses sensi/variab/gravité restent 100% humaines. Cette skill ne fait QUE préparer les paramètres.
