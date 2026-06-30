# Architecture — releaf-acv

## Principe directeur : pipeline idempotente + versioning par projet

Chaque projet EPD est un **dossier versionné** dans OneDrive. Chaque skill prend `projet/v_n/` en
entrée et écrit dans `projet/v_n+1/` — **jamais en place**. Une exécution = un **snapshot complet
rejouable**. Une modification (trame, FE, commentaire vérif) → on relance la chaîne → un nouveau
snapshot apparaît, comparable au précédent via `diff-versions-projet`.

C'est ce qui fait passer les 3 cycles de vérification de « jours » à « heures », et ce qui donne
l'**auditabilité ISO** automatique (snapshots + logs).

## Les 5 couches

### C1 · Déterministe (Python pur, sans LLM)
Reproductible, testable, auditable pour la revue critique. Chaque run logge dans `_logs/`.
`generer-trame-collecte`, `valider-fichier-collecte`, `convertir-unites`, `generer-import-simapro`,
`post-traiter-export-simapro`, `extraire-parametres-analyses`, `generer-fiche-fdes`,
`snapshot-projet`, `diff-versions-projet`, `propager-changement-donnee`, `regenerer-tableaux-impactes`.

> ⚠️ `extraire-parametres-analyses` **ne fait pas** les analyses sensi/variab/gravité (= 100 %
> humain). Elle prépare seulement les paramètres à réinjecter dans SimaPro.

### C2 · Mixte (Python + LLM) — l'IA suggère, le praticien valide
Nourrie des référentiels **INIES** et de la **norme** (ISO 14025/14067, EN 15804).
`verifier-coherence-donnees`, `formaliser-hypotheses`, `preparer-checklist-justificatifs`,
`matcher-fe-anciennes-missions`, `identifier-paragraphes-impactes`, `classer-commentaires-verif`,
`expliquer-commentaires-verif`.

### C3 · Rédactionnelle (LLM + template Word verrouillé)
`rediger-rapport-accompagnement`, `rediger-fiche-fdes-narrative`, `mettre-a-jour-narratif-cible`,
`preparer-reponses-verificateurs`.

### C4 · Agents orchestrateurs
`mener-une-epd`, `preparer-import-simapro`, `generer-livrables-epd`, `repondre-revue-critique`,
`auditer-epd-passee`.

### C5 · Connecteur MCP
OneDrive / SharePoint (dossiers projets versionnés) + filesystem Cowork (workspace temporaire).

## Flow · cycle de vérification (1 itération AR)

`classer-commentaires-verif` trie en 3 voies :

- **Cosmétique** (wording, typo) → `mettre-a-jour-narratif-cible`.
- **Data** (valeur/FE/hypothèse) → `propager-changement-donnee` → re-modélisation SimaPro (manuel) →
  `regenerer-tableaux-impactes` → `identifier-paragraphes-impactes` → `mettre-a-jour-narratif-cible`.
- **Méthodo** → remontée humaine (Nathan), pas d'auto.

Puis `snapshot-projet` → `diff-versions-projet` → `preparer-reponses-verificateurs`.

## Roadmap (5 vagues)

1. **Sem. 1-2** — Repo + squelette plugin · reverse engineering import SimaPro · convention OneDrive.
2. **Sem. 3-6** — `generer-import-simapro` (POC) · `valider-fichier-collecte` · `snapshot-projet`.
3. **Mois 2-3** — agent `preparer-import-simapro` · `post-traiter-export-simapro` · `extraire-parametres-analyses`.
4. **Mois 4-6** — `rediger-rapport-accompagnement` · `generer-fiche-fdes` · agent `mener-une-epd`.
5. **Mois 5-8** — `diff-versions-projet` · cascade (`propager-changement-donnee` + `regenerer-tableaux-impactes`) · mise à jour ciblée · agent `repondre-revue-critique`.

**Objectifs :** première rédaction −40 à −50 % ; cycle de vérif −60 à −70 % (le gain le plus massif).

## Décisions à trancher (vague 1)

- ✅ **Convention de nommage / arborescence OneDrive** — **tranchée (2026-06-29)**. Modèle imbriqué :
  `client/produit/v_n/` (versioning + snapshots) avec, dans chaque `v_n/`, les 6 dossiers d'étape.
  Voir [`referentiels/conventions-onedrive.md`](referentiels/conventions-onedrive.md).
- **Template Word « à slots »** (Nathan + Arthur) — placeholders tableaux + tags chiffres + section visuels/client.
- **Format des logs skills** (Arthur + Nathan) — JSON ou Markdown, présentable au vérificateur.
- **Emplacement standard du bilan massique** dans chaque projet.
- **Robustesse si la trame de collecte est modifiée** (structure changée).
- **Table d'affectation des FE** pour la réutilisation (même produit/famille ; gérer les FE modifiés à la main).
