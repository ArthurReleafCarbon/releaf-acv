# Convention arborescence & nommage OneDrive

> ✅ **Validée** (réu équipe, 2026-06-29). Source de vérité de l'organisation des projets EPD/FDES.
> Conditionne le contrat entrée/sortie de **toutes les skills**. Toute évolution = PR (owner Arthur).
> Version lisible par machine : [`arborescence-fdes.json`](arborescence-fdes.json).

## 1. Principe : deux niveaux

L'organisation combine **versioning** (colonne vertébrale technique) et **structure métier**
(lisibilité humaine), sans que l'un casse l'autre.

- **Niveau versioning** — chaque projet est une suite de dossiers `v_n/`. Un `v_n/` est un
  **snapshot complet et rejouable** du projet à un instant donné. Les skills lisent `projet/v_n/`
  et écrivent `projet/v_n+1/` — **jamais en place** (cf. `ARCHITECTURE.md`). C'est ce qui donne
  l'idempotence, `snapshot-projet`, `diff-versions-projet` et l'auditabilité ISO.
- **Niveau métier** — **à l'intérieur de chaque `v_n/`**, le travail est rangé dans les **6 dossiers
  d'étape** validés (l'arbo d'Evane). Chaque snapshot contient donc l'intégralité des 6 dossiers.

> ⚠️ Il n'y a **plus** de `Tour 1/2/3` dans `5. Vérification/`. Le versioning des tours de revue est
> porté par le niveau `v_n/` (un tour de vérif = un nouveau snapshot). Cela évite le doublon
> « Tour n » vs « v_n ».

## 2. Emplacement & portabilité du chemin

Le chemin absolu dépend de chaque poste (`/Users/<user>/Library/CloudStorage/OneDrive-…` sur Mac,
`C:\Users\<user>\…` sur Windows). **On ne hardcode jamais le chemin absolu.** On résout
dynamiquement la racine de la bibliothèque SharePoint, puis on y ajoute un chemin **relatif**
identique sur tous les postes.

Ordre de résolution de la racine (à implémenter dans le connecteur C5, cf. roadmap #10) :

1. Variable d'environnement `RELEAF_ONEDRIVE_ROOT` (override explicite, prioritaire).
2. Auto-détection macOS : `~/Library/CloudStorage/OneDrive-ReleafCarbon*/Releaf Carbon - Documents`.
3. Auto-détection Windows : `%USERPROFILE%/Releaf Carbon - Documents` (ou dossier synchronisé équivalent).

Chemins **relatifs** (depuis la racine `Releaf Carbon - Documents`) :

| Usage | Chemin relatif |
|---|---|
| Projets clients (missions) | `2. Commercial/1. Missions en cours/` |
| Dossier-type / template | `2. Commercial/1. Missions en cours/0. Dossier client FDES/` |
| Template de référence (legacy) | `5. Outils/13. Automatisation FDES/Dossier FDES/` |

## 3. Nommage

```
2. Commercial/1. Missions en cours/
  <client>/                 ← kebab-case (ex. alphapro)
    <produit>/              ← kebab-case (ex. performance-plus)
      v1-initiale/          ← première version livrée au vérificateur
      v2-verif1/            ← snapshot après 1er aller-retour vérificateur
      v3-verif2/
      v4-final/             ← version finale (import INIES)
```

Règles :

- **kebab-case** partout (dossiers, fichiers) — cohérent avec `CONTRIBUTING.md`.
- Version = `v{n}` + label court optionnel (`-initiale`, `-verif1`, `-final`). `n` strictement croissant.
- Un projet = `<client>/<produit>`. Multi-produit d'un même client = plusieurs sous-dossiers produit.

## 4. Les 6 dossiers d'étape (dans CHAQUE `v_n/`)

| # | Dossier | Contenu principal |
|---|---------|-------------------|
| 1 | `1. Collecte de données` | Trame de collecte remplie, données brutes client, **bilan massique** (emplacement standard) |
| 2 | `2. Modélisation` | `Modélisation.xlsx`, fichier d'import SimaPro, export SimaPro brut |
| 3 | `3. Rapport et FDES` | Rapport d'accompagnement, fiche FDES |
| 4 | `4. Résultats et analyses` | Tableaux ICV consolidés, tableur résultats, analyses sensi/variabilité/gravité (**100 % humain**) |
| 5 | `5. Vérification` | Commentaires du vérificateur, réponses, justificatifs (un tour = un `v_n`) |
| 6 | `6. Import INIES` | Fichier d'import INIES |

Plus, au **niveau `v_n/`** (hors des 6 dossiers) :

- `_logs/` — traces d'exécution des skills (auditabilité ISO). Format à figer (roadmap #3, owner Arthur).

> **Bilan massique** : placé dans `1. Collecte de données/`. À confirmer définitivement (roadmap #4,
> owner Evane) ; si déplacé, mettre à jour cette section **et** le manifest.

## 5. Comportement & idempotence

- **Jamais de modification en place.** Une modif (trame, FE, commentaire vérif) → on relance la
  chaîne → un nouveau `v_n+1/` apparaît, comparable au précédent via `diff-versions-projet`.
- Une skill qui lit `v_n/` doit retrouver les 6 dossiers aux noms **exacts** ci-dessus (accents
  compris). Si la structure attendue est absente ou modifiée : **alerter, ne pas deviner** (roadmap
  #5, robustesse trame modifiée).
- Les chemins internes au plugin utilisent `${CLAUDE_PLUGIN_ROOT}` ; les chemins projet sont résolus
  via la racine OneDrive (§2), jamais en dur.

## 6. Pour les développeurs de skills

Ne pas redéclarer les chemins à la main : lire [`arborescence-fdes.json`](arborescence-fdes.json),
qui est la **source unique** des noms de dossiers, du nommage de version et de la logique de
résolution de chemin.
