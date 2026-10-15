# TP2 : Blockchain simple en Python

Ce TP met en pratique les concepts fondamentaux de la blockchain avec Python (sans bibliothèque externe, utilisation de `hashlib`).

## Contenu des exercices

1. **`exercice1.py`** : Découverte de la fonction de hachage cryptographique **SHA-256** et observation de l'effet d'avalanche.
2. **`exercice2.py`** : Création de la classe `Bloc` avec calcul automatique du hash.
3. **`exercice3.py`** : Construction d'une chaîne de 3 blocs liés par leurs empreintes (`previous_hash`).
4. **`exercice4.py`** : Implémentation de la fonction de vérification de l'intégrité de la blockchain (`verifier_blockchain`).
5. **`exercice5.py`** : Ajout d'un 4ème bloc et validation de la chaîne complète.
6. **`exercice6.py`** : Expérimentations d'altération et falsification (modification d'un bloc intermédiaire, recalcul des hash, tentative de contournement).

## Exécution

Pour exécuter un exercice avec Python :

```bash
py exercice1.py
```
*(ou `python exercice1.py` selon votre configuration système)*
