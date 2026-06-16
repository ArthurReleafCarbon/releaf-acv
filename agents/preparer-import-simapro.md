---
name: preparer-import-simapro
description: >
  Enchaîne la validation de la trame puis la génération de l'import SimaPro.
  <example>Contexte : EPD en cours. user: « lance preparer-import-simapro pour … » → l'agent enchaîne les skills ci-dessous.</example>
---

# Agent · preparer-import-simapro

> 🚧 **STUB** — à compléter. Owner : **Arthur**.

**Couche :** C4 · Agent orchestrateur
**Owner :** Arthur
**Statut :** `à faire`

## Rôle

Enchaîne la validation de la trame puis la génération de l'import SimaPro.

## Enchaînement de skills

```
valider-fichier-collecte → convertir-unites → generer-import-simapro
```

## Garde-fous

- L'agent **orchestre** des skills existantes, il n'invente rien.
- À chaque étape sensible : **point de contrôle praticien** avant de continuer.
- Ne jamais imposer : proposer, attendre validation.
- Respecte la pipeline idempotente (v_n → v_n+1).
