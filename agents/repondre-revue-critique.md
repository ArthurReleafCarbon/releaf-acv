---
name: repondre-revue-critique
description: >
  Orchestre un cycle de vérification : tri des commentaires → cascade data → mise à jour narratif → réponses.
  <example>Contexte : EPD en cours. user: « lance repondre-revue-critique pour … » → l'agent enchaîne les skills ci-dessous.</example>
---

# Agent · repondre-revue-critique

> 🚧 **STUB** — à compléter. Owner : **Vincent**.

**Couche :** C4 · Agent orchestrateur
**Owner :** Vincent
**Statut :** `à faire`

## Rôle

Orchestre un cycle de vérification : tri des commentaires → cascade data → mise à jour narratif → réponses.

## Enchaînement de skills

```
classer-commentaires-verif → [data: propager-changement-donnee → regenerer-tableaux-impactes → identifier-paragraphes-impactes → mettre-a-jour-narratif-cible] / [cosmétique: mettre-a-jour-narratif-cible] / [méthodo: remontée humaine] → snapshot-projet → diff-versions-projet → preparer-reponses-verificateurs
```

## Garde-fous

- L'agent **orchestre** des skills existantes, il n'invente rien.
- À chaque étape sensible : **point de contrôle praticien** avant de continuer.
- Ne jamais imposer : proposer, attendre validation.
- Respecte la pipeline idempotente (v_n → v_n+1).
