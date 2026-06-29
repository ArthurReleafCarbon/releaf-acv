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

**Couche** : C1 partagee. La validation est en Python pur deterministe (valider_collecte.py), auditable et reproductible pour la revue critique ISO. Claude n'intervient que pour l'I/O et l'orchestration, jamais dans le jugement des controles.
**Owner :** Thilas
**Statut :** `V1`

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

**Procédure pour Claude**
1. Recuperer la trame remplie depuis projet/v_n/ via le connecteur OneDrive ; l'ecrire en local (ex. /tmp/trame.xlsx).
2. Executer : python valider_collecte.py /tmp/trame.xlsx /tmp/sortie --tol 0.02.
  - La tolerance du bilan massique est un parametre (--tol), jamais une constante en dur.
3. Lire le code retour du processus : 0 = OK, 2 = BLOQUANT, 1 = erreur technique.
4. Televerser /tmp/sortie/alertes-validation.md et /tmp/sortie/_logs/*.json dans projet/v_n+1/ (jamais en place dans v_n/ : pipeline idempotente).
5. Restituer au praticien : code retour, nombre d'alertes par gravite, et le rappel que les 🟠 sont des points a lever, pas des blocages automatiques.

**Controles exécutés (Python)**
1. Format / structure : presence des 10 onglets attendus (dont l'onglet cache Bilan Massique) ; en-tetes des onglets tabulaires conformes. Onglet manquant ou en-tete renommee = 🔴. Comparaison robuste aux accents et a la casse.
2. Completude : champs obligatoires non vides (config CHAMPS_OBLIGATOIRES). DUVP exclue (decision actee).
3. Coherence des unites : appartenance a une liste blanche (config UNITES_AUTORISEES). Pas de conversion ici (role de convertir-unites).
4. Bilan massique : lit TOTAL ENTRANTS (C12) et TOTAL SORTANTS (C20) de l'onglet Bilan Massique, gardes par verification du libelle (B12, B20). Recalcule l'ecart relatif en Python : |sortants - entrants| / entrants <= tol. Hors tolerance = 🔴.
5. Ordres de grandeur : valeurs nulles, negatives ou hors bornes (config BORNES).


## Format de sortie (`alertes-validation.md`)

Regrouper par gravité :

- 🔴 **Bloquant** — empêche un import fiable (ex. bilan massique faux, onglet manquant).
- 🟠 **À vérifier** — n'empêche pas l'import mais doit être levé avec le client
  (ex. conso élec. suspecte, champ DUVP manquant).
- 🟢 **Info** — remarques mineures.

Chaque alerte : `gravité · onglet/cellule · description · action suggérée`.

## Garde-fous (posture Releaf — CR 20/05)

- **L'IA exécute, elle ne propose pas d'elle-même et n'impose jamais.** La skill **signale**, elle ne **corrige pas** les données du client.
- Une alerte 🟠 n'est **pas un blocage** : c'est au praticien de décider de continuer ou de revenir vers le client.
- **Pipeline idempotente** : lit `projet/v_n/`, écrit dans `projet/v_n+1/` — jamais en place.
- Skill **déterministe** (Python pur) : reproductible et auditable pour la revue critique. Chaque run logge dans `_logs/`.

## Notes

- Première skill candidate au POC (vague 2) avec `generer-import-simapro`.
- Le seuil de tolérance du bilan massique doit être un paramètre, pas une constante en dur.
