---
name: generer-livrables-epd
description: >
  Enchaîne le post-traitement de l'export puis la rédaction des livrables.
  <example>Contexte : EPD en cours. user: « lance generer-livrables-epd pour … » → l'agent enchaîne les skills ci-dessous.</example>
---

# Agent · generer-livrables-epd

> 🚧 **STUB** — à compléter. Owner : **Nathan**.

**Couche :** C4 · Agent orchestrateur
**Owner :** Nathan
**Statut :** `à faire`

## Rôle

Enchaîne le post-traitement de l'export puis la rédaction des livrables.

## Enchaînement de skills

```
post-traiter-export-simapro → extraire-parametres-analyses → rediger-rapport-accompagnement → generer-fiche-fdes
```

## Garde-fous

- L'agent **orchestre** des skills existantes, il n'invente rien.
- À chaque étape sensible : **point de contrôle praticien** avant de continuer.
- Ne jamais imposer : proposer, attendre validation.
- Respecte la pipeline idempotente (v_n → v_n+1).
