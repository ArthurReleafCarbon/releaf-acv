---
name: auditer-epd-passee
description: >
  Revue d'une EPD existante (contrôle a posteriori).
  <example>Contexte : EPD en cours. user: « lance auditer-epd-passee pour … » → l'agent enchaîne les skills ci-dessous.</example>
---

# Agent · auditer-epd-passee

> 🚧 **STUB** — à compléter. Owner : **Nathan**.

**Couche :** C4 · Agent orchestrateur
**Owner :** Nathan
**Statut :** `à faire`

## Rôle

Revue d'une EPD existante (contrôle a posteriori).

## Enchaînement de skills

```
diff-versions-projet + verifier-coherence-donnees sur une EPD archivée
```

## Garde-fous

- L'agent **orchestre** des skills existantes, il n'invente rien.
- À chaque étape sensible : **point de contrôle praticien** avant de continuer.
- Ne jamais imposer : proposer, attendre validation.
- Respecte la pipeline idempotente (v_n → v_n+1).
