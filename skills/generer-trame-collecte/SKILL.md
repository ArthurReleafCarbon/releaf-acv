---
name: generer-trame-collecte
description: Génère la trame de collecte Excel adaptée au scénario du projet (mono/multi produit, mono/multi site). À utiliser au démarrage d'une EPD, quand on dit « générer la trame de collecte », « créer le fichier de collecte ».
---

# generer-trame-collecte

> 🚧 **STUB** — squelette à compléter. Owner : **Thomas**.

**Couche :** C1 · Déterministe
**Owner :** Thomas
**Statut :** `à faire`

## Objectif

Produire le fichier de collecte client, avec les bons onglets et colonnes attendus par le format d'import SimaPro, selon le scénario.

## Entrées / Sorties

- **Entrées :** scénario (mono/multi), produit, site
- **Sorties :** trame-collecte.xlsx

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

Génération auto des onglets selon le scénario. CRUD lignes/onglets paramétrable.
