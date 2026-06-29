# Carte du gabarit `base_collecte_fdes.xlsx`

Référence interne pour le skill. Toutes les éditions structurelles visent ces ancres.
Vérifier ces positions au runtime (la base peut évoluer) plutôt que de les supposer.

## Palette (hex, sans préfixe FF)
- Bandeau section : `2E5E3A` (texte blanc)
- En-tête colonne : `D6E4D0`
- Cellule à remplir (jaune) : `FFF6CC`
- Cellule verrouillée / BE (gris) : `ECECEC`
- Note : `F5F5F5`
- Bandeau rappel année : `FFF2CC`
- Police : Arial

## Noms définis (ne pas casser)
- `AnneeRef` = `'1. Société et site'!$C$16`
- `ListeProduits` = `'2. Vos produits'!$A$5:$A$54` (plage des références produit ; conservée comme repère, plus utilisée comme source de déroulant)

## Onglets (ordre actuel)
`0. Mode d'emploi` | `1. Société et site` | `2. Vos produits` | `3. Composition des produits` | `4. Matières auxilliaires` | `5. Énergie - Eau` | `6. Déchets` | `7. Rejets air-eau (GEREP)` | `8. Emballages` | `9. Livraison et fin de vie`

> Défauts connus et conservés (décision client) : doublon du bloc "produits consommés" en bas de l'onglet 3 ; numérotation des titres internes désynchronisée ; "auxilliaires" mal orthographié ; sommaire de l'onglet 0 désynchronisé ; eau réduite à une ligne ; déroulants absents dans la base. Le skill NE corrige PAS la base. Le fichier de sortie ne contient AUCUNE liste déroulante (décision Thomas) : les unités et valeurs attendues sont écrites en clair dans les libellés.

## Ancres par onglet

### 0. Mode d'emploi
Bandeau A1. Mini-table "Où trouver" en-tête ligne 8. Sommaire des onglets en colonne B. Note A26.
- Adaptation : si un onglet est retiré, retirer la ligne correspondante du sommaire.

### 1. Société et site
Bandeau A1. Sections A3 / A9 / A15. `AnneeRef` en C16.
- Quasi jamais dépendant du produit. Ne pas toucher sauf demande.

### 2. Vos produits  ← onglet d'attributs produit principal
En-tête colonnes : ligne 4. Saisie : lignes 5 à 54.
Colonnes : A Référence | B Nom commercial | C Description | **D Longueur (mm)** | **E Largeur (mm)** | **F Épaisseur / hauteur (mm)** | G Masse d'une unité (kg) | H Unité de vente | I Quantité fabriquée sur l'année | J Unité de cette quantité | K Commentaire.
- **Cœur de l'adaptation** : remplacer/compléter les colonnes D-E-F par les attributs dimensionnels propres au produit (ex : isolant → Épaisseur (mm) / R (m².K/W) / λ (W/m.K) ; tuyau → Diamètre (mm) / Longueur (mm) ; menuiserie → Uw / dimensions). Adapter `u_vente` et `u_qte` au produit.
- Unités attendues, en clair dans le libellé : Unité de vente (ex : tonne / kg / pièce / ml), Unité de quantité (ex : tonnes / kg / pièce).

### 3. Composition des produits
Bloc 1 (nomenclature) : en-tête ligne 5, saisie 6→46.
Colonnes : A Référence produit (texte, à recopier depuis l'onglet 2) | B Matière / composant | C Masse pour 1 unité (kg) | D Matière recyclée ? | E Fournisseur | F Ville | G Pays | H Source | I Commentaire.
Bloc 2 (doublon "produits consommés") : en-tête ligne 49 (redondant avec l'onglet 4).
- Adaptation : valeurs attendues en clair (D Matière recyclée ? : Oui / Non / Inconnu ; H Source). Les lignes matières restent VIDES (contenu interdit).

### 4. Matières auxilliaires
En-tête ligne 5, saisie 6→20.
Colonnes : A Matière auxiliaire | B Fonction / usage | C Quantité / an | D Unité | E Fournisseur | F Ville | G Pays | H Source | I Commentaire.
- Unités/valeurs en clair : D Unité (kg / L / pièce / m³), H Source.

### 5. Énergie - Eau
En-tête colonnes ligne 4 (A vide | B Type d'énergie | C Valeur | D Unité | E Source | F Commentaire).
Sections (bandeaux) ~A5 Combustibles, ~A13 Électricité, ~A18 Engins, ~A23/A26 Eau.
- Adaptation : ajuster les libellés de lignes de combustible/électricité pertinents au procédé (ex : "Four de cuisson" pour céramique/terre cuite, "Étuve" pour béton, "Presse / extrudeuse" pour plasturgie) en tant que **champs vides**. Si l'eau process est significative pour le produit, ré-éclater la ligne "Eau" en sources (réseau / forage / recyclée).
- Unités en clair : D Unité (kWh PCS / kWh PCI / MWh / m³ / L ; m³ ou L pour l'eau), E Source.

### 6. Déchets
En-tête ligne 4, saisie à partir de ligne 5. Col A contient des types suggérés (liste indicative de la base).
Colonnes : A Type | B Dangereux ? | C Quantité | D Unité | E Mode d'élimination | F Source | G Commentaire.
- Adaptation : ajuster les types de déchets de procédé pertinents (libellés, pas de quantités). Valeurs en clair : B Dangereux ? (Oui / Non), D Unité (kg / tonnes), E Filière (recyclage, valorisation énergétique, enfouissement, réemploi), F Source.

### 7. Rejets air-eau (GEREP)
Question GEREP en C4 (réponse en clair : Oui / Non / Je ne sais pas). Bloc air : en-tête ligne 8, lignes 9→21. Bloc eau : en-tête ligne 24, lignes 25→33.
- Adaptation : retirer les lignes non pertinentes au procédé. Ex : "CO2 process (décarbonatation / réactions)" ne concerne que terre cuite / ciment / chaux ; COV surtout peintures / colles / solvants. Conserver le caractère conditionnel GEREP.
- Valeur en clair : E Source.

### 8. Emballages
En-tête ligne 4, lignes 5→12. Col B = libellés d'éléments, saisie C:F.
- Adaptation : ajuster les éléments d'emballage typiques (palette, housse, cerclage, calage) en champs vides selon le conditionnement du produit.

### 9. Livraison et fin de vie
Bandeau A1. Sections A5 Livraison, A9 Durée de vie, A13 Fin de vie. Saisie en C.
- Valeurs en clair : transport principal (camion / train / bateau / mixte), fin de vie (recyclé / réemployé / enfoui / incinéré).
- Adaptation : les valeurs de fin de vie peuvent être restreintes au produit (ex : métal → Recyclé ; inerte → Enfoui).
