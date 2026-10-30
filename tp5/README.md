# TP5 : Cryptographie Asymétrique et Signatures Numériques dans la Blockchain

**Auteur :** Ahmed Channoufi  
**Environnement :** Python 3.13 (`cryptography` library / Ed25519)

Ce TP explore les fondements de la cryptographie asymétrique appliquée aux transactions blockchain : la génération de paires de clés (publique/privée), la signature numérique, la structure d'un portefeuille cryptographique, l'intégrité et la vérification des transactions, ainsi que la prévention de l'usurpation d'identité et de la fraude.

---

## Structure des Exercices

- [`exercice1.py`](file:///c:/blockchain/tp5/exercice1.py) : **Génération d'une paire de clés Ed25519**
  - Utilisation de `cryptography.hazmat.primitives.asymmetric.ed25519`.
  - Génération de la clé privée et extraction de la clé publique au format Raw octets / hexadécimal (32 octets = 64 caractères hexadécimaux).

- [`exercice2.py`](file:///c:/blockchain/tp5/exercice2.py) : **Signature numérique d'un message**
  - Signature d'un message encodé en UTF-8 à l'aide de la clé privée (`cle_privee.sign(...)`).
  - Observation de la signature Ed25519 (64 octets = 128 caractères hexadécimaux).

- [`exercice3.py`](file:///c:/blockchain/tp5/exercice3.py) : **Vérification d'une signature numérique**
  - Vérification cryptographique via `cle_publique.verify(signature, message)`.
  - Gestion de l'exception `InvalidSignature` en cas d'altération du message, de la signature ou de mauvaise clé publique.

- [`exercice4.py`](file:///c:/blockchain/tp5/exercice4.py) : **Classe `Portefeuille`**
  - Encapsulation de la clé privée secrète (`_cle_privee`) et exposition de la clé publique.
  - Définition de l'adresse du portefeuille comme l'empreinte hexadécimale de la clé publique brute.
  - Méthode `signer(message)` déléguant la signature à la clé privée.

- [`exercice5.py`](file:///c:/blockchain/tp5/exercice5.py) : **Classe `Transaction` et signature**
  - Représentation standardisée d'une transaction (`expediteur`, `destinataire`, `montant`).
  - Sérialisation déterministe via `json.dumps(..., sort_keys=True, separators=(',', ':'))`.
  - Contrôle d'autorisation strict : seul le portefeuille correspondant à l'adresse de l'expéditeur peut signer.

- [`exercice6.py`](file:///c:/blockchain/tp5/exercice6.py) : **Vérification autonome des transactions**
  - Ajout de la méthode `verifier_signature()` sur `Transaction`.
  - Reconstitution de la clé publique `Ed25519PublicKey` depuis les octets hexadécimaux de l'adresse de l'expéditeur.
  - Détection automatique de toute altération de contenu (montant, destinataire, expéditeur).

- [`exercice7.py`](file:///c:/blockchain/tp5/exercice7.py) : **Validation complète (Signature + Soldes)**
  - Fonctions `valider_transaction(transaction, soldes)` et `executer_transaction(transaction, soldes)`.
  - Vérification conjointe de la validité cryptographique (signature intacte) et de la solvabilité financière (solde suffisant, montant positif).

- [`exercice8.py`](file:///c:/blockchain/tp5/exercice8.py) : **Étude de cas : Tentative d'usurpation d'identité**
  - Simulation d'un acteur malveillant (Bob) tentant de dépenser les fonds d'Alice sans sa clé privée.
  - Démonstration de l'impossibilité mathématique d'usurper une transaction valide sans détenir le secret de la clé privée.

---

## Instructions d'Exécution

```powershell
# Exécuter les exercices individuellement
py c:\blockchain\tp5\exercice1.py
py c:\blockchain\tp5\exercice2.py
py c:\blockchain\tp5\exercice3.py
py c:\blockchain\tp5\exercice4.py
py c:\blockchain\tp5\exercice5.py
py c:\blockchain\tp5\exercice6.py
py c:\blockchain\tp5\exercice7.py
py c:\blockchain\tp5\exercice8.py
```
