# Contrat de structure (log de génération)

Ce document définit le **contrat** entre `generer-trame-collecte` (producteur) et
`verifier-trame-collecte` (consommateur).

`generer-trame-collecte` écrit un log Markdown dans `_logs/`. Ce log commence par un
**frontmatter YAML** à schéma fixe (bloc délimité par `---`), suivi du texte libre destiné
à l'humain. Le validateur ne lit **que** le frontmatter : c'est lui qui décrit la structure
réellement appliquée à la trame, et donc ce que le validateur doit attendre du fichier rempli.

Sans ce frontmatter (absent ou illisible), le validateur ne peut pas connaître la structure
attendue : il s'arrête en **erreur technique** (code retour 1), il ne produit pas de faux 🔴.

## Schéma

```yaml
---
schema_version: 1

# Scénario du projet
scenario:
  produits: mono            # mono | multi
  sites: mono               # mono | multi

# Produit / procédé (traçabilité, sert au rapprochement fichier <-> log)
produit:
  type: "isolant PSE"
  procede: "extrusion"

# Onglets réellement présents dans la trame générée (ordre indifférent)
onglets_presents:
  - "0. Mode d'emploi"
  - "1. Société et site"
  - "2. Vos produits"
  - "3. Composition des produits"
  - "4. Consommations usines"
  - "5. Déchets"
  - "6. Emballages"
  - "7. Utilisation"
  - "8. Livraison et fin de vie"

# Onglets retirés car sans objet pour ce produit (info, non contrôlé)
onglets_retires: []

# Onglet 2 : colonnes d'attributs adaptées au produit (D, E, F... variables)
# Le validateur vérifie que ces en-têtes existent et ne sont pas renommés.
colonnes_produit:
  - col: D
    libelle: "Épaisseur (mm)"
    obligatoire: false
  - col: E
    libelle: "R (m².K/W)"
    obligatoire: false
  - col: F
    libelle: "λ (W/m.K)"
    obligatoire: false

# Champs obligatoires par onglet (liste de colonnes). Sert à la Famille 2 (complétude).
# La colonne A d'un onglet tabulaire = clé de ligne ; sa présence rend la ligne "active".
champs_obligatoires:
  "2. Vos produits": [A, G, H, I, J]
  "3. Composition des produits": [A, B, C]

# Postes d'énergie (onglet 4) rendus obligatoires pour ce procédé (libellés col A)
postes_energie_obligatoires:
  - "Électricité du réseau"

# Listes blanches d'unités par onglet.colonne (Famille 3).
# Ne cibler QUE des colonnes qui contiennent une unité (pas les colonnes de masse
# où l'unité est déjà figée dans l'en-tête, ex. onglet 3 col C « ... (kg) »).
unites_attendues:
  "4. Consommations usines":
    C: ["kWh", "MWh", "kWh PCS", "kWh PCI", "m³", "L"]
  "5. Déchets":
    C: ["kg", "tonnes", "t"]

# Valeurs fermées autorisées par onglet.colonne (Famille 3)
valeurs_fermees:
  "3. Composition des produits":
    D: ["Oui", "Non", "Inconnu"]

# Bornes de plausibilité par onglet.colonne (Famille 5). Facultatif.
bornes:
  "2. Vos produits":
    G: {min: 0, max: 100000}
---
```

## Règles de lecture côté validateur

- **Champs obligatoires du schéma** : `schema_version`, `onglets_presents`. Absents = erreur technique.
- **Champs facultatifs** : si `bornes`, `valeurs_fermees`, `unites_attendues`,
  `postes_energie_obligatoires` sont absents, le contrôle correspondant est **sauté** (pas d'alerte),
  et le rapport le signale en 🟢 (contrôle non effectué faute de contrat).
- **Ancrage** : les positions de lignes d'en-tête sont des invariants du gabarit (voir
  `generer-trame-collecte/reference/base_layout.md`), pas dans le contrat. Le contrat ne porte que
  ce qui **varie selon le produit**.
- Le validateur ne modifie jamais le contrat ni la trame. Il lit, il signale.
