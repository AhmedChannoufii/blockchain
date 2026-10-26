# TP3 : Minage et Proof of Work : sécuriser une blockchain avec Python

Ce TP approfondit le fonctionnement d'une blockchain en introduisant le mécanisme de consensus **Proof of Work (Preuve de Travail)**, la notion de **nonce** et le concept de **difficulté**.

## Objectifs d'apprentissage
- Comprendre le rôle du **minage** et de la preuve de travail.
- Manipuler la variable **nonce** pour altérer le hash sans modifier les transactions.
- Observer l'impact exponentiel de la **difficulté** sur le temps de calcul.
- Sécuriser la chaîne de blocs contre la falsification rétroactive.
- Analyser les limites (consommation énergétique, attaque 51%).

---

## Contenu des exercices

| Fichier | Titre | Description |
|---|---|---|
| [`exercice1.py`](exercice1.py) | Recherche d'un hash avec zéros | Découverte de la recherche par force brute d'un hash débutant par `"000"` avec "Blockchain" puis "Bitcoin". |
| [`exercice2.py`](exercice2.py) | Mesure de la difficulté | Minage selon différentes difficultés (1 à 4 zéros) et chronométrage avec `time.perf_counter()`. |
| [`exercice3.py`](exercice3.py) | Classe `Bloc` avec PoW | Intégration de l'attribut `nonce` et de la méthode `miner_bloc(difficulte)`. |
| [`exercice4.py`](exercice4.py) | Minage d'une chaîne de 3 blocs | Construction d'une séquence de 3 blocs minés successivement avec difficulté 3. |
| [`exercice5.py`](exercice5.py) | Vérification avec Proof of Work | Fonction `verifier_blockchain()` à 3 niveaux : contenu, preuve de travail et chaînage. |
| [`exercice6.py`](exercice6.py) | Courbe et analyse de performance | Relevé des temps/tentatives et tracé du graphique Matplotlib (`graphique_difficulte.png`). |
| [`exercice7.py`](exercice7.py) | Étude de cas (coût d'une attaque) | Simulation d'une tentative de falsification du bloc 2 et coût du re-minage en cascade. |

---

## Exécution des scripts

Depuis le dossier `tp3/` :
```powershell
py exercice1.py
py exercice2.py
py exercice3.py
py exercice4.py
py exercice5.py
py exercice6.py
py exercice7.py
```

## Auteur
Ahmed Channoufi
