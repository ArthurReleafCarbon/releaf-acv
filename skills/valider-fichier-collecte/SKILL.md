---
name: valider-fichier-collecte
description: >
  Valide un fichier de collecte rempli par le client avant l'import SimaPro : format, complétude,
  cohérence des unités et bilan massique. Produit un rapport d'alertes, sans jamais corriger
  les données d'autorité. Déclencher sur « valider la trame de collecte », « contrôler le fichier
  reçu », « vérifier le bilan massique », « est-ce que cette collecte est exploitable ».
---

# valider-fichier-collecte

> ✅ **Skill de référence — entièrement rédigée comme patron.** Copier cette structure pour les autres skills.

**Couche :** C1 · Déterministe (Python pur, sans LLM — auditable pour la vérif ISO)
**Owner :** Nathan
**Statut :** `spécifiée` (implémentation Python à faire — vague 2)

## Objectif

Contrôler qu'un fichier de collecte rempli par le client est **exploitable** avant de lancer
`generer-import-simapro`. La skill **ne corrige rien** : elle signale. Les alertes sont des
**points à lever par le praticien** (souvent en revenant vers le client), pas des blocages.

## Entrées / Sorties

- **Entrées :**
  - `trame-collecte-<produit>.xlsx` (version remplie par le client), lue dans `projet/v_n/`
  - le scénario du projet (mono/multi produit, mono/multi site) — déduit de la trame ou passé en argument
- **Sorties (écrites dans `projet/v_n+1/`) :**
  - `alertes-validation.md` — rapport lisible des alertes, classées par gravité
  - entrée dans `_logs/valider-fichier-collecte_<timestamp>.json` (auditabilité ISO)
- **Code retour :** `OK` (exploitable, éventuelles alertes non bloquantes) / `BLOQUANT` (à corriger avant import)

## Contrôles à effectuer

1. **Format / structure**
   - Tous les onglets attendus pour le scénario sont présents (cf. `generer-trame-collecte`).
   - Les colonnes obligatoires existent et sont nommées correctement.
   - ⚠️ **Si la structure a été modifiée par le client** (onglet ajouté, colonne déplacée/renommée) :
     ne pas planter — émettre une alerte explicite et lister les écarts. *(point à trancher, cf. CONTRIBUTING)*

2. **Complétude**
   - Champs obligatoires non vides (ex. durée de vie du produit / DUVP).
   - Lister chaque champ manquant avec son onglet et sa cellule.

3. **Cohérence des unités**
   - Chaque valeur a une unité attendue ; signaler les unités inattendues.
   - Ne pas convertir ici — la conversion est le rôle de `convertir-unites`.

4. **Bilan massique**
   - Vérifier : `Σ intrants ≈ Σ produits + Σ déchets` (tolérance paramétrable, ex. ±2 %).
   - Exemple attendu : `1 020 kg intrants = 1 000 kg produit + 20 kg déchets` ✓.
   - Le fichier bilan massique doit être au **même emplacement standard** dans tous les projets
     (cf. `referentiels/conventions-onedrive.md`).

5. **Ordres de grandeur** *(léger ici ; analyse fine = `verifier-coherence-donnees`)*
   - Repérer les valeurs nulles, négatives, ou hors bornes physiques évidentes.

## Format de sortie (`alertes-validation.md`)

Regrouper par gravité :

- 🔴 **Bloquant** — empêche un import fiable (ex. bilan massique faux, onglet manquant).
- 🟠 **À vérifier** — n'empêche pas l'import mais doit être levé avec le client
  (ex. conso élec. suspecte, champ DUVP manquant).
- 🟢 **Info** — remarques mineures.

Chaque alerte : `gravité · onglet/cellule · description · action suggérée`.

## Étapes d'implémentation

1. Lire la trame depuis `projet/v_n/` (via le connecteur MCP OneDrive).
2. Charger les attendus du scénario (onglets/colonnes obligatoires).
3. Exécuter les 5 familles de contrôles ; accumuler les alertes.
4. Écrire `alertes-validation.md` dans `projet/v_n+1/`.
5. Écrire le log JSON dans `_logs/`.
6. Retourner le code (`OK` / `BLOQUANT`) à l'agent appelant.

## Garde-fous (posture Releaf — CR 20/05)

- **L'IA exécute, elle ne propose pas d'elle-même et n'impose jamais.** La skill **signale**, elle ne **corrige pas** les données du client.
- Une alerte 🟠 n'est **pas un blocage** : c'est au praticien de décider de continuer ou de revenir vers le client.
- **Pipeline idempotente** : lit `projet/v_n/`, écrit dans `projet/v_n+1/` — jamais en place.
- Skill **déterministe** (Python pur) : reproductible et auditable pour la revue critique. Chaque run logge dans `_logs/`.

## Notes

- Première skill candidate au POC (vague 2) avec `generer-import-simapro`.
- Le seuil de tolérance du bilan massique doit être un paramètre, pas une constante en dur.