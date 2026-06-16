# Contribuer à releaf-acv

Guide pour développer une skill. Pas besoin d'être dev chevronné : une skill = un dossier + un
`SKILL.md` clair. Le patron de référence est
[`skills/valider-fichier-collecte/SKILL.md`](skills/valider-fichier-collecte/SKILL.md).

## La posture, d'abord

Avant d'écrire une ligne, garder en tête le cadre (CR 20/05) :

- **L'IA exécute, elle ne propose pas d'elle-même, elle n'impose jamais.** Une skill **suggère** ou
  **prépare** ; le praticien décide. Toute sortie est un **brouillon à contrôler**.
- **Ne pas automatiser pour automatiser.** Si une skill ne fait pas vraiment gagner de temps ou
  fragilise la qualité, on ne la fait pas.
- **Contrôle & diligence** : toujours vérifier données, wording et résultat.
- Ce qui reste **100 % humain** : sélection des FE, analyses sensi/variab/gravité, wording de la
  revue critique, arbitrages méthodo.

## Workflow Git

1. Créer une branche : `git checkout -b skill/<nom-de-la-skill>`.
2. Travailler dans `skills/<nom>/` (ou `agents/<nom>.md`).
3. Commit messages clairs en français : `feat(valider-fichier-collecte): contrôle bilan massique`.
4. Ouvrir une **Pull Request** vers `main`. Arthur relit et merge.

> Seul **Arthur** push/merge sur `main`. Tout le monde passe par une PR. On ne committe **jamais**
> de données client (cf. `.gitignore`).

## Anatomie d'une skill

Chaque `SKILL.md` contient :

- **Frontmatter YAML** : `name` (kebab-case = nom du dossier) et `description` à la **3e personne**
  avec des **phrases déclencheuses** concrètes (« déclencher sur … »).
- **Couche / Owner / Statut** (`à faire` → `spécifiée` → `implémentée` → `testée`).
- **Objectif** en une phrase.
- **Entrées / Sorties** explicites (fichiers lus dans `v_n/`, écrits dans `v_n+1/`).
- **Étapes** (algorithme pour C1, prompt + garde-fous pour C2/C3).
- **Garde-fous** (reprendre le bloc posture).
- **Notes** éventuelles.

## Règles techniques

- **Idempotence** : lire `projet/v_n/`, écrire `projet/v_n+1/`. Jamais modifier en place.
- **Logs** : chaque exécution écrit une trace dans `_logs/` (auditabilité ISO).
- **Déterminisme C1** : Python pur, pas d'appel LLM, résultat reproductible et testable.
- **Chemins** : utiliser `${CLAUDE_PLUGIN_ROOT}` pour toute référence interne au plugin, jamais de
  chemin absolu en dur.
- **kebab-case** partout (dossiers, fichiers).
- **Référentiels** (ratios, INIES, norme) : dans `referentiels/`, modifiés via PR (owner Arthur).

## Définition de « terminé » pour une skill

- [ ] `SKILL.md` complet (toutes les sections du patron).
- [ ] Implémentation faite et **testée sur une EPD passée réelle**.
- [ ] Respecte l'idempotence et logge dans `_logs/`.
- [ ] Garde-fous explicites ; sortie = brouillon contrôlable.
- [ ] PR relue par Arthur.

## Questions ouvertes (à trancher en équipe — cf. ARCHITECTURE.md)

Convention OneDrive, template Word à slots, format des logs, emplacement du bilan massique,
robustesse trame modifiée, table d'affectation des FE.
