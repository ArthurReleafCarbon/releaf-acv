# releaf-acv

Plugin **Cowork** de Releaf Carbon pour automatiser la **mécanique répétitive** de la modélisation
ACV / EPD autour de SimaPro.

> **Posture (non négociable).** Le plugin est un **outil**. C'est nous qui avons la main : l'IA
> **exécute**, elle ne propose pas d'elle-même et **n'impose jamais**. Elle peut suggérer ; le
> praticien challenge, valide, corrige. Le savoir-faire et l'expertise restent humains.
> On ne cherche **pas à tout automatiser** — seulement ce qui fait gagner du temps sans dégrader la qualité.

## Ce que fait le plugin

Le praticien parle à Claude en français, comme à un collègue. Claude lance les bonnes skills et
agents selon le contexte. Tout ce qui touche au **métier** (sélection des FE dans SimaPro, analyses
de sensibilité / variabilité / gravité, wording de la revue critique, arbitrages méthodo) **reste
100 % humain**.

## Pour qui

Les 5 collaborateurs de Releaf installent le plugin et l'utilisent dans Cowork. Personne n'a besoin
de coder pour s'en servir. Le développement des skills, lui, se fait dans ce repo.

## Installation (utilisateurs)

Le plugin est distribué depuis ce repo GitHub privé. Arthur installe la première version sur chaque
poste (ou envoie le lien). Aucune manipulation manuelle.

## Architecture en bref

5 couches (détail dans [`ARCHITECTURE.md`](ARCHITECTURE.md)) :

| Couche | Type | Rôle |
|--------|------|------|
| C1 | Déterministe (Python pur) | Calculs reproductibles, auditables ISO |
| C2 | Mixte (Python + LLM) | L'IA suggère, le praticien valide |
| C3 | Rédactionnelle (LLM + template) | Génération de contenu Word, template verrouillé |
| C4 | Agents | Sub-agents qui enchaînent les skills |
| C5 | Connecteur MCP | Lecture/écriture des fichiers projets (OneDrive) |

**Principe directeur :** pipeline **idempotente** + **versioning par projet**. Chaque skill lit
`projet/v_n/` et écrit `projet/v_n+1/`, jamais en place. Une exécution = un snapshot rejouable.

## Hébergement

- **Le code** (ce repo) : skills, agents, `plugin.json`, templates Word vierges, référentiels embarqués.
- **Les fichiers projets EPD** : dans **OneDrive Releaf** (`projets/client/produit/v_n/`). **Aucune
  donnée client n'est committée ici** (cf. `.gitignore`).

## Qui fait quoi — répartition des skills

> Proposition de départ, à ajuster en équipe. Chacun est **owner** de ses skills (les implémente, les teste).

| Owner | Workstream | Skills / agents |
|-------|-----------|-----------------|
| **Arthur** (data, lead tech) | Pipeline import/export + matching FE | `generer-import-simapro`, `post-traiter-export-simapro`, `matcher-fe-anciennes-missions`, agent `preparer-import-simapro` |
| **Ewan** (dev full stack) | Infra déterministe & versioning | `convertir-unites`, `snapshot-projet`, `diff-versions-projet`, `propager-changement-donnee`, `regenerer-tableaux-impactes`, connecteur MCP |
| **Nathan** (ACV/EPD/FDES) | Collecte, FDES & rédaction | `generer-trame-collecte`, `valider-fichier-collecte`, `extraire-parametres-analyses`, `generer-fiche-fdes`, `formaliser-hypotheses`, `identifier-paragraphes-impactes`, `rediger-rapport-accompagnement`, `rediger-fiche-fdes-narrative`, `mettre-a-jour-narratif-cible`, `preparer-reponses-verificateurs`, agents `mener-une-epd` & `generer-livrables-epd` |
| **Vincent** (bilan carbone/SBTi) | Vérification | `verifier-coherence-donnees`, `classer-commentaires-verif`, `expliquer-commentaires-verif`, agents `repondre-revue-critique` & `auditer-epd-passee` |
| **Guillaume** (commercial) | Relation client | `preparer-checklist-justificatifs` |

➡️ Le détail (statut, entrées/sorties, TODO) est dans chaque `skills/<nom>/SKILL.md`.
➡️ Pour commencer à contribuer : [`CONTRIBUTING.md`](CONTRIBUTING.md). Patron de référence :
[`skills/valider-fichier-collecte/SKILL.md`](skills/valider-fichier-collecte/SKILL.md).

## État d'avancement

🚧 Squelette posé (juin 2026). La plupart des skills sont des **stubs** à compléter selon la roadmap
(5 vagues, cf. `ARCHITECTURE.md`). Priorité vague 1 : reverse engineering de l'import SimaPro +
convention OneDrive.
