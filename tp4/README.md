# TP4 : Transactions et validation dans une blockchain avec Python

Ce TP traite de la structure des **transactions**, de la **gestion des soldes**, de la validation contre la **double dépense** et du regroupement de plusieurs transactions au sein de blocs chaînés et minés.

---

## Contenu des exercices

| Fichier | Titre | Description |
|---|---|---|
| [`exercice1.py`](exercice1.py) | Représentation d'une transaction | Classe `Transaction` (expéditeur, destinataire, montant) et méthode d'affichage. |
| [`exercice2.py`](exercice2.py) | Gestion des soldes | Dictionnaire des soldes, transferts et vérification de la conservation de la masse monétaire. |
| [`exercice3.py`](exercice3.py) | Validation d'une transaction | Fonction `valider_transaction()` testant l'existence des utilisateurs, montants positifs et solde suffisant. |
| [`exercice4.py`](exercice4.py) | Exécution sécurisée | Fonction `executer_transaction()` qui ne met à jour les comptes qu'après validation. |
| [`exercice5.py`](exercice5.py) | Transactions en attente (Mempool) | Tri d'une liste de transactions en attente entre transactions acceptées et rejetées. |
| [`exercice6.py`](exercice6.py) | Bloc multi-transactions | Classe `Bloc` contenant une liste de transactions, sérialisation déterministe JSON et calcul du hash. |
| [`exercice7.py`](exercice7.py) | Blockchain multi-transactions | Chaîne de 3 blocs minés contenant plusieurs transactions et test de falsification. |
| [`exercice8.py`](exercice8.py) | Étude de cas (Double dépense) | Simulation de deux transferts concurrents d'Alice et comparaison selon l'ordre d'arrivée. |

---

## Exécution des scripts

Depuis le dossier `tp4/` :
```powershell
py exercice1.py
py exercice2.py
py exercice3.py
py exercice4.py
py exercice5.py
py exercice6.py
py exercice7.py
py exercice8.py
```

## Auteur
Ahmed Channoufi
