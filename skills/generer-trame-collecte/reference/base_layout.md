# Carte du gabarit `base_collecte_fdes.xlsx`

Référence interne pour le skill. Toutes les éditions structurelles visent ces ancres.
Vérifier ces positions au runtime (la base peut évoluer) plutôt que de les supposer.

## Palette (hex, sans préfixe FF)
- Bandeau section : `2E5E3A` (texte blanc)
- En-tête colonne : `D6E4D0`
- Cellule à remplir (jaune) : `FFF6CC`
- Cellule verrouillée / libellé (gris) : `ECECEC`
- Note : `F5F5F5`
- Bandeau rappel année : `FFF2CC` (texte `9C5700`)
- Police : Arial

## Noms définis (ne pas casser)
- `AnneeRef` = `'1. Société et site'!$B$16`
- `ListeProduits` = `'2. Vos produits'!$A$5:$A$54` (plage des références produit ; conservée comme repère, plus utilisée comme source de déroulant)

## Onglets (ordre actuel)
`0. Mode d'emploi` | `1. Société et site` | `2. Vos produits` | `3. Composition des produits` | `4. Consommations usines` | `5. Déchets` | `6. Emballages` | `7. Utilisation` | `8. Livraison et fin de vie`

> Défauts connus et conservés (la base est la source de vérité, le skill NE corrige PAS la base) :
> - Aucune liste déroulante dans la base. Le fichier de sortie ne contient AUCUNE liste déroulante (décision Thomas) : les unités et valeurs attendues sont écrites en clair dans les libellés.

## Ancres par onglet

### 0. Mode d'emploi
Bandeau A1. Bloc « Objet » A3 / B3. Bloc « Comment remplir » A5 / B5. Table « Où trouver chaque donnée » : bandeau A7, en-tête A8 / B8, lignes A9→A12 (Composition, Consommations usines, Déchets, Emballages). Sommaire des onglets : bandeau A14, liste en **colonne A** (A15→A22). Note de bas A25.
- Adaptation : si un onglet est retiré, retirer la ligne correspondante du sommaire (colonne A) et, le cas échéant, de la table « Où trouver ».

### 1. Société et site
Bandeau A1 « 1. Votre société et votre site ». Bloc société A4→A7 (raison sociale, référent, email, tél). Bloc site A10→A13 (nom site, adresse, référent site, contact). `AnneeRef` en **B16** (libellé A16). Version du document B18 (libellé A18). Date de remplissage A19. Saisie en colonne B (fusion B:C).
- Quasi jamais dépendant du produit. Ne pas toucher sauf demande.

### 2. Vos produits  ← onglet d'attributs produit principal
En-tête colonnes : ligne 4. Saisie : lignes 5 à 54.
Colonnes : A Référence interne / code | B Nom commercial | C Description / usage | **D Longueur (mm)** | **E Largeur (mm)** | **F Épaisseur / hauteur (mm)** | G Masse d'une unité (kg) | H Unité de vente | I Quantité fabriquée sur l'année | J Unité de cette quantité | K Quantité perdue lors de la fabrication | L Commentaire.
- **Cœur de l'adaptation** : remplacer/compléter les colonnes D-E-F par les attributs dimensionnels propres au produit (ex : isolant → Épaisseur (mm) / R (m².K/W) / λ (W/m.K) ; tuyau → Diamètre (mm) / Longueur (mm) ; menuiserie → Uw / dimensions). Adapter les unités de vente et de quantité au produit.
- Unités attendues, en clair dans le libellé : Unité de vente (ex : tonne / kg / pièce / ml), Unité de quantité (ex : tonnes / kg / pièce).

### 3. Composition des produits
Bandeau A1 « 3. De quoi sont faits vos produits ».
Bloc 1 (nomenclature) : sous-bandeau A3, note A4, en-tête ligne 5, saisie 6→46.
Colonnes : A Référence produit (texte, à recopier depuis l'onglet 2) | B Matière / composant | C Masse pour 1 unité de produit (kg) | D Matière recyclée ? | E Fournisseur | F Ville du fournisseur | G Pays | H Source de l'information | I Commentaire.
Bloc 2 (produits consommés) : sous-bandeau A47 « Produits consommés en fabrication mais NON présents dans le produit fini », note A48, en-tête ligne 49, saisie 50→59.
Colonnes bloc 2 : A Nom du produit | B Quantité consommée sur l'année | C Unité | D Fournisseur | E Pays | F Source | G Commentaire.
- Adaptation : valeurs attendues en clair (D Matière recyclée ? : Oui / Non / Inconnu ; H Source). Les lignes matières restent VIDES (contenu interdit). Le bloc 2 remplace de fait l'ancien onglet « Matières auxiliaires ».

### 4. Consommations usines
Bandeau A1 « 4. Vos consommables d'usines ». En-tête colonnes ligne 4 : A Type d'énergie | B Valeur | C Unité | D Source | E Commentaire.
Sections (bandeaus) : A5 Combustibles (A6→A11), A13 Électricité (A14→A16), A18 Carburant des engins restant sur le site (A19→A21), A23 Autres consommations usine (A24 Eau, A25 Réfrigérant). Note A27 (le transport routier longue distance est hors périmètre site).
- Adaptation : ajuster les libellés de lignes de combustible / électricité pertinents au procédé (ex : « Four de cuisson » pour céramique / terre cuite, « Étuve » pour béton, « Presse / extrudeuse » pour plasturgie) en tant que **champs vides**. Si l'eau process est significative, ré-éclater la ligne « Eau ».
- Unités en clair : C Unité (kWh PCS / kWh PCI / MWh / m³ / L ; m³ ou L pour l'eau), D Source.

### 5. Déchets
Bandeau A1 « 5. Vos déchets ». En-tête ligne 4, saisie à partir de ligne 5. Col A contient des types suggérés (liste indicative de la base).
Colonnes : A Type de déchet | B Quantité | C Unité | D Mode d'élimination / valorisation | E Source | F Commentaire.
- Adaptation : ajuster les types de déchets de procédé pertinents (libellés, pas de quantités). Valeurs en clair : C Unité (kg / tonnes), D Filière (recyclage, valorisation énergétique, enfouissement, réemploi), E Source.

### 6. Emballages
Bandeau A1 « 6. Vos emballages ». En-tête ligne 4 : A Élément | B Valeur | C Unité / précision | D Source | E Commentaire. Libellés d'éléments en **colonne A** (A5→A12 : masse produit sur palette type, palette bois, palette perdue/consignée, film PE, cerclage/feuillard, coins/intercalaires carton, emballage primaire, autre).
- Adaptation : ajuster les éléments d'emballage typiques selon le conditionnement du produit (champs vides).

### 7. Utilisation
Bandeau A1 « 7. Utilisation du produit ». Note A3 rappelant le caractère **optionnel** de chaque section.
Cinq sections, chacune : bandeau (A:E) + ligne d'aide (note grise) + en-tête colonnes + 4 lignes de saisie jaunes.
- Sections : A5 Utilisation, A13 Maintenance, A21 Réparation, A29 Remplacement, A37 Réhabilitation.
- En-tête colonnes (lignes 7 / 15 / 23 / 31 / 39) : A Matière / composant | B Masse (kg) | C Nombre d'occurrences sur la durée de vie | D Distance de livraison (km) | E Source / Commentaire.
- Caractère optionnel signalé uniquement par la note A3 (pas de suffixe « (optionnel) » dans les bandeaus).
- Adaptation : ajuster / retirer les sections non pertinentes au produit ; les lignes de saisie restent VIDES.

### 8. Livraison et fin de vie
Bandeau A1 « 8. Livraison et fin de vie ». Sections : A5 Livraison de vos produits (B6 Distance site → client (km) - Camion, B7 - Bateau), A9 Fin de vie (B10). La section « Durée de vie du produit » a été retirée de la base.
- Valeurs en clair : transport (km par mode), fin de vie (recyclé / réemployé / enfoui / incinéré).
- Adaptation : les valeurs de fin de vie peuvent être restreintes au produit (ex : métal → Recyclé ; inerte → Enfoui).
