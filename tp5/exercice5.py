# TP5 - Exercice 5 : Creer une transaction signee
# Ahmed Channoufi

import json
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

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
            raise ValueError("Portefeuille non autorise : seul l'expediteur peut signer sa transaction !")
        self.signature = portefeuille.signer(self.obtenir_message())

print("=== EXERCICE 5 : Transaction signee ===")

# Creation des portefeuilles
alice = Portefeuille()
bob = Portefeuille()
charlie = Portefeuille()

# 1. Transaction legitime : Alice -> Bob (20 unites) signee par Alice
print("\n--- Test 1 : Transaction d'Alice vers Bob, signee par Alice ---")
t1 = Transaction(alice.obtenir_adresse(), bob.obtenir_adresse(), 20)
t1.signer(alice)
print("Expediteur   :", t1.expediteur)
print("Destinataire :", t1.destinataire)
print("Montant      :", t1.montant)
print("Signature    :", t1.signature.hex()[:40] + "...")

# 2. Transaction legitime : Bob -> Charlie (10 unites) signee par Bob
print("\n--- Test 2 : Transaction de Bob vers Charlie, signee par Bob ---")
t2 = Transaction(bob.obtenir_adresse(), charlie.obtenir_adresse(), 10)
t2.signer(bob)
print("Expediteur   :", t2.expediteur)
print("Destinataire :", t2.destinataire)
print("Montant      :", t2.montant)
print("Signature    :", t2.signature.hex()[:40] + "...")

# 3. Tentative de piratage : Bob tente de signer une transaction d'Alice
print("\n--- Test 3 : Bob tente de signer une transaction dont l'expediteur est Alice ---")
t_fraude = Transaction(alice.obtenir_adresse(), bob.obtenir_adresse(), 50)
try:
    t_fraude.signer(bob)
    print("Succes (anormal)")
except ValueError as e:
    print("Tentative bloquee avec succes !")
    print("Exception levee :", e)

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Pourquoi une transaction doit-elle etre signee ?")
print("-> Pour prouver mathematiquement que le detenteur des fonds a personnellement approuve ce transfert.")

print("\nQ2 : Pourquoi le message signe contient-il l'expediteur, le destinataire et le montant ?")
print("-> Pour figer tous les parametres de l'echange. Si le destinataire ou le montant change,")
print("   la signature devient invalide.")

print("\nQ3 : Pourquoi utilisons-nous json.dumps() avec sort_keys=True ?")
print("-> Pour produire une chaine de texte deterministe. Sans tri des cles, deux dictionnaires")
print("   identiques pourraient avoir un ordre different et generer des octets distincts.")

print("\nQ4 : Quel est le role de la methode signer() de la classe Transaction ?")
print("-> Elle verifie d'abord que le portefeuille presente appartient bien a l'expediteur,")
print("   puis produit la signature sur le json de la transaction.")

print("\nQ5 : Pourquoi verifions-nous que l'adresse du portefeuille correspond a celle de l'expediteur ?")
print("-> Pour empecher immediatement un utilisateur tiers (ex: Bob) de tenter de signer avec sa propre")
print("   cle privee une transaction qui depenserait les fonds d'Alice.")
