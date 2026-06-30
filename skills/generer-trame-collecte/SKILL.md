---
name: generer-trame-collecte
description: Génère la trame de collecte Excel adaptée au scénario du projet (mono/multi produit). À utiliser au démarrage d'une EPD, quand on dit « générer la trame de collecte », « créer le fichier de collecte ».
---

# generer-trame-collecte

>Owner : **Thomas**.

**Couche :** C1 · Déterministe
**Owner :** Thomas
**Statut :** `v1 (à valider)`

## Objectif

Produire le fichier de collecte client à partir du gabarit validé, en l'adaptant au type de produit. La sortie est une trame de collecte de données brutes, destinée à un industriel non familier de l'ACV (langage métier, cellules jaunes à remplir). Ce n'est pas un fichier d'import SimaPro : la transformation vers SimaPro est une étape aval, hors de ce skill.

## Entrées / Sorties

- **Entrées :** scénario (mono/multi), type de produit et procédé, contexte projet lu dans `projet/v_n/`. Gabarit de référence : `templates/base_collecte_fdes.xlsx` (du skill).
- **Sorties :** `projet/v_n+1/trame-collecte-{produit}-{usine}.xlsx` + changelog + trace dans `_logs/`. Les variables `{produit}` et `{usine}` sont substituées par les valeurs lues dans le contexte projet (`projet/v_n/`), en minuscules sans accents ni espaces (remplacés par `-`).

## Règle d'or : STRUCTURE, pas CONTENU

Le skill modifie des **champs**, jamais des données.

| Autorisé (structure) | Interdit (contenu) |
|---|---|
| Ajouter / renommer / retirer une colonne d'attribut | Écrire une valeur dans une cellule de saisie |
| Ajouter une ligne à libellé **vide** pertinente (ex : « Four de cuisson ») | Lister la nomenclature réelle du produit |
| Préciser l'**unité ou la valeur attendue** en clair dans le libellé | Renseigner un fournisseur, une conso, une distance |
| Retirer un onglet ou une ligne non pertinents | Pré-cocher un scénario fin de vie |

## Étapes

1. **Lire le contexte.** Charger le scénario et le contexte produit/site depuis projet/v_n/. Si l'information manque ou est ambiguë, poser UNE question de clarification. Ne pas deviner.
2. **Inférer le profil de structure** (inférence libre, voir reference/base_layout.md pour les positions exactes) : attributs produit (onglet 2), produits consommés en fabrication (onglet 3, bloc 2), postes d'énergie / consommations propres au procédé (onglet 4), déchets de procédé (onglet 5), emballages (onglet 6), sections d'usage pertinentes (onglet 7 : utilisation, maintenance, réparation, remplacement, réhabilitation), vocabulaire fin de vie (onglet 8), onglets ou sections sans objet à retirer (+ ligne du sommaire onglet 0). La base ne contient plus d'onglet rejets air-eau (GEREP).
3. **Présenter le diff pour validation.** Lister, par onglet, les changements de structure prévus. Attendre l'accord du praticien. Ne rien écrire avant validation.
4. **Appliquer.** Copier l'asset vers le fichier de travail (jamais éditer l'asset).
   Écrire un court script pilote important `scripts/adapt_collecte.py` (primitives :
   `add_input_column`, `set_colheaders`, `set_header_text`, `add_labelled_rows`,  `delete_rows`, `delete_sheet`, `strip_all_dropdowns`). Réutiliser les noms définis  `AnneeRef` et `ListeProduits`. **Aucune liste déroulante** : appeler  `strip_all_dropdowns(wb)` en fin de traitement pour purger toute validation héritée.
   Les unités et valeurs attendues (ex : « tonnes / kg / pièce », « Oui / Non »)  s'écrivent **en clair dans le libellé de colonne ou de ligne**. Conserver palette, bandeaux, rappel d'année, formatage.
5. **Recalculer et vérifier.** python /mnt/skills/public/xlsx/scripts/recalc.py <fichier> 60. Exiger zéro erreur. Vérifier qu'aucune cellule de saisie n'a été pré-remplie.
6. **Écrire la sortie en v_n+1/** + log. Sortir dans projet/v_n+1/, jamais en place.
Écrire une trace dans _logs/ (scénario, produit, diff appliqué, horodatage).
Joindre une section À vérifier par le consultant : Unité fonctionnelle candidate, en pistes à vérifier, jamais affirmées.

## Garde-fous (posture Releaf — CR 20/05)

- **L'IA exécute, elle ne propose pas d'elle-même et n'impose jamais.** La sortie est un **brouillon à contrôler** par le praticien.
- Le praticien garde la main : il challenge, valide, corrige. Le savoir-faire reste humain.
- **Pipeline idempotente** : la skill lit `projet/v_n/`, écrit dans `projet/v_n+1/` — **jamais en place**.
- Chaque exécution écrit une trace dans `_logs/` (auditabilité ISO 14025 / 14067 / EN 15804).
- **Aucune liste déroulante** : la trame de sortie ne contient aucune validation de
  données. Les unités et valeurs attendues sont écrites en clair dans les libellés.
- **Langage client** : tout libellé visible reste en langage métier, sans terme ACV (pas de
  A1/A3, module, UF, allocation).


## Notes

Génération auto des onglets selon le scénario. CRUD lignes/onglets paramétrable.
