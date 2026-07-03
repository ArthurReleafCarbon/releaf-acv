---
name: verifier-trame-collecte
description: >
  Vérifie qu'une trame de collecte remplie par le client est exploitable avant l'import SimaPro :
  intégrité structurelle, complétude, cohérence, bilan massique produit, ordres de grandeur.
  Produit un rapport d'alertes classé par gravité, sans jamais corriger les données du client.
  Déclencher sur « vérifier la trame de collecte », « contrôler le fichier reçu », « valider la
  collecte », « est-ce que cette collecte est exploitable », « vérifier le bilan massique ».
---

# verifier-trame-collecte

**Couche :** C1 · Déterministe (Python pur, `scripts/verifier_collecte.py`). Auditable et reproductible pour la revue critique ISO. Claude n'intervient que pour l'I/O et l'orchestration, jamais dans le jugement des contrôles.
**Owner :** Thomas
**Statut :** `v1`

## Objectif

Contrôler qu'une trame de collecte **remplie par le client** est exploitable avant de lancer `generer-import-simapro`. La skill **ne corrige rien** : elle signale. Les alertes sont des points à lever par le praticien (souvent en revenant vers le client), pas des blocages automatiques.

La structure de la trame **varie selon le produit** (colonnes d'attributs de l'onglet 2, libellés de lignes, sections et onglets retirés). Le validateur ne devine pas cette structure : il la lit dans le **log de génération** produit par `generer-trame-collecte` (frontmatter YAML). Voir `reference/contrat-structure.md`.

## Entrées / Sorties

- **Entrées :**
  - `trame-collecte-{produit}-{usine}.xlsx` remplie par le client, lue dans `projet/v_n/`.
  - le **log de génération** correspondant (`.md` avec frontmatter YAML), qui décrit la structure attendue.
  - paramètres : `--tol` (tolérance bilan massique, défaut 0.02), `--seuil-dur` (seuil bloquant, défaut 0.10).
- **Sorties (écrites dans `projet/v_n+1/`) :**
  - `alertes-validation.md` : rapport lisible classé par gravité.
  - trace `_logs/verifier-trame-collecte_{timestamp}.md` (frontmatter YAML, auditabilité ISO).
- **Code retour :** `0` OK (exploitable) / `2` BLOQUANT (au moins un 🔴) / `1` erreur technique (trame illisible, contrat absent/invalide).

## Procédure pour Claude

1. Récupérer la trame remplie et son log de génération depuis `projet/v_n/` (connecteur OneDrive), les écrire en local (ex. `/tmp/trame.xlsx`, `/tmp/log.md`).
2. Exécuter : `python scripts/verifier_collecte.py /tmp/trame.xlsx /tmp/log.md /tmp/sortie --tol 0.02 --seuil-dur 0.10`.
   - La tolérance et le seuil bloquant sont des **paramètres**, jamais des constantes en dur.
3. Lire le code retour : 0 = OK, 2 = BLOQUANT, 1 = erreur technique.
4. Si code 1 : le log de génération est absent ou son frontmatter YAML est illisible. Ne pas produire de faux 🔴 : signaler au praticien que la structure attendue est inconnue.
5. Téléverser `/tmp/sortie/alertes-validation.md` et `/tmp/sortie/_logs/*.md` dans `projet/v_n+1/` (jamais en place dans `v_n/`).
6. Restituer au praticien : code retour, nombre d'alertes par gravité, rappel que les 🟠 sont des points à lever, pas des blocages.

## Contrôles exécutés (Python, déterministes)

**Famille 0 · Prérequis.** Log de génération présent, frontmatter YAML parsable (`schema_version` et `onglets_presents` requis). Sinon erreur technique (code 1), pas de faux 🔴.

**Famille 1 · Intégrité structurelle.** Onglets présents = onglets attendus par le contrat (manquant → 🔴, non prévu → 🟠). Noms définis `AnneeRef` et `ListeProduits` intacts (→ 🔴). En-têtes fixes de l'onglet 2 (Référence, Masse, Unités, Quantité) et colonnes d'attributs produit du contrat, présents et non renommés (→ 🔴). Comparaison robuste aux accents et à la casse.

**Famille 2 · Complétude.** Année de référence renseignée (→ 🔴). Champs obligatoires du contrat non vides sur les lignes actives (→ 🔴). Postes d'énergie déclarés obligatoires renseignés (→ 🔴). Champs Source vides (→ 🟠, traçabilité).

**Famille 3 · Cohérence interne.** Références produit de l'onglet 3 présentes dans l'onglet 2 (orpheline → 🔴). Chaque produit déclaré a au moins une ligne de composition (→ 🔴). Unités dans la liste blanche du contrat (→ 🟠, pas de conversion ici, rôle de `convertir-unites`). Valeurs fermées conformes (→ 🟠).

**Famille 4 · Bilan massique produit.** Somme des masses composants (onglet 3) vs masse d'une unité déclarée (onglet 2), par produit. Écart ≤ `tol` → 🟢 ; `tol` < écart ≤ `seuil-dur` → 🟠 ; écart > `seuil-dur` → 🔴. Le bilan massique **site/annuel est hors périmètre v1**.

**Famille 5 · Ordres de grandeur.** Valeur négative sur masse/quantité (→ 🔴, impossible physiquement). Masse d'une unité nulle (→ 🔴, bloque le calcul). Hors bornes du contrat (→ 🟠).

## Format de sortie (`alertes-validation.md`)

Regroupé par gravité :

- 🔴 **Bloquant** : empêche un import fiable (onglet manquant, bilan massique faux, produit sans composition).
- 🟠 **À vérifier** : n'empêche pas l'import mais doit être levé avec le client (source manquante, unité à convertir).
- 🟢 **Info** : remarques mineures, contrôles non effectués faute de contrat.

Chaque alerte : `gravité · onglet/cellule · description · action suggérée`.

## Garde-fous (posture Releaf)

- **La skill signale, elle ne corrige jamais** les données du client.
- Un 🟠 n'est **pas un blocage** : c'est au praticien de décider de continuer ou de revenir vers le client.
- **Pipeline idempotente** : lit `projet/v_n/`, écrit dans `projet/v_n+1/`, jamais en place.
- **Déterministe** (Python pur) : reproductible et auditable pour la revue critique. Chaque run logge dans `_logs/`.
- La tolérance et le seuil bloquant du bilan massique sont des **paramètres**, jamais des constantes en dur.
- Le validateur **dépend du log de génération** : sans contrat de structure lisible, il ne valide pas (code 1).

## Notes

- Remplace l'ancienne skill `valider-fichier-collecte`.
- Dépend du contrat de structure émis par `generer-trame-collecte` (voir `reference/contrat-structure.md`).
- Candidate au POC (vague 2) avec `generer-import-simapro`.
