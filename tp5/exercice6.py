# TP5 - Exercice 6 : Verifier une transaction signee
# Ahmed Channoufi

import json
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey
)
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

class Portefeuille:
    def __init__(self):
        self.cle_privee = Ed25519PrivateKey.generate()
        self.cle_publique = self.cle_privee.public_key()

    def obtenir_adresse(self):
        cle_bytes = self.cle_publique.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        return cle_bytes.hex()

    def signer(self, message):
        return self.cle_privee.sign(message.encode("utf-8"))

class Transaction:
    def __init__(self, expediteur, destinataire, montant):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.montant = montant
        self.signature = None

    def obtenir_message(self):
        donnees = {
            "expediteur": self.expediteur,
            "destinataire": self.destinataire,
            "montant": self.montant
        }
        return json.dumps(
            donnees,
            sort_keys=True,
            separators=(",", ":")
        )

    def signer(self, portefeuille):
        if portefeuille.obtenir_adresse() != self.expediteur:
            raise ValueError("Portefeuille non autorise")
        self.signature = portefeuille.signer(self.obtenir_message())

    def verifier_signature(self):
        if self.signature is None:
            return False

        try:
            cle_bytes = bytes.fromhex(self.expediteur)
            cle_publique = Ed25519PublicKey.from_public_bytes(cle_bytes)
            cle_publique.verify(
                self.signature,
                self.obtenir_message().encode("utf-8")
            )
            return True
        except (InvalidSignature, ValueError):
            return False

print("=== EXERCICE 6 : Verification de la signature d'une transaction ===")

# Creation des portefeuilles
alice = Portefeuille()
bob = Portefeuille()
charlie = Portefeuille()

# 1. Transaction normale valide
t = Transaction(alice.obtenir_adresse(), bob.obtenir_adresse(), 20)
t.signer(alice)

print("\n--- Test 1 : Transaction originale valide ---")
print("Signature valide avant modification :", t.verifier_signature())

# 2. Modification du montant apres signature (20 -> 200 unites)
t.montant = 200
print("\n--- Test 2 : Modification du montant apres signature (20 -> 200) ---")
print("Signature valide apres modif montant :", t.verifier_signature())

# 3. Retablissement du montant et modification du destinataire
t.montant = 20
t.destinataire = charlie.obtenir_adresse()
print("\n--- Test 3 : Modification du destinataire apres signature (Bob -> Charlie) ---")
print("Signature valide apres modif dest   :", t.verifier_signature())

# 4. Transaction sans aucune signature
t_non_signee = Transaction(alice.obtenir_adresse(), bob.obtenir_adresse(), 20)
print("\n--- Test 4 : Transaction non signee (signature = None) ---")
print("Signature valide transaction vierge :", t_non_signee.verifier_signature())

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Pourquoi la methode verifier_signature() utilise-t-elle la cle publique ?")
print("-> Parce que la cle publique suffit pour verifier mathematiquement la signature,")
print("   sans avoir besoin de connaitre la cle privee secrete de l'expediteur.")

print("\nQ2 : Pourquoi la signature est-elle verifiee sur le contenu de la transaction ?")
print("-> Pour s'assurer que le contenu verifie correspond exactement a ce que l'expediteur")
print("   avait approuve lors de la signature.")

print("\nQ3 : Que se passe-t-il si le montant est modifie apres la signature ?")
print("-> Le json regenere n'a plus les memes octets, donc cle_publique.verify() echoue")
print("   et la methode renvoie immediatement False.")

print("\nQ4 : Pourquoi une transaction sans signature doit-elle etre refusee dans notre modele ?")
print("-> Parce que rien ne prouve que l'expediteur a consenti au virement. Sans signature,")
print("   n'importe qui pourrait debiter le compte d'Alice a son insu.")

print("\nQ5 : Une signature valide suffit-elle a garantir qu'une transaction peut etre executee ? Justifiez.")
print("-> Non ! Une signature valide prouve l'authenticite et le consentement, mais elle ne dit pas")
print("   si l'expediteur possede reellement le solde necessaire. Il faut aussi verifier le solde.")
