# TP5 - Exercice 4 : Creer une classe Portefeuille
# Ahmed Channoufi

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

class Portefeuille:
    def __init__(self):
        # Chaque portefeuille cree sa propre cle privee secrete
        self.cle_privee = Ed25519PrivateKey.generate()
        self.cle_publique = self.cle_privee.public_key()

    def obtenir_adresse(self):
        # L'adresse publique correspond a la cle publique en hexadecimal
        cle_bytes = self.cle_publique.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        return cle_bytes.hex()

    def signer(self, message):
        return self.cle_privee.sign(
            message.encode("utf-8")
        )

print("=== EXERCICE 4 : Classe Portefeuille (Wallet) ===")

# Creation des trois portefeuilles demandes
alice = Portefeuille()
bob = Portefeuille()
charlie = Portefeuille()

print("\n--- Adresses publiques des portefeuilles ---")
print("Adresse Alice   :", alice.obtenir_adresse())
print("Adresse Bob     :", bob.obtenir_adresse())
print("Adresse Charlie :", charlie.obtenir_adresse())

# Alice signe un message
msg_alice = "Alice envoie 20 unites a Bob"
sig_alice = alice.signer(msg_alice)

print("\n--- Signature produite par Alice ---")
print("Message signe   :", msg_alice)
print("Signature Alice :", sig_alice.hex())

# Bob signe un message
msg_bob = "Bob envoie 10 unites a Charlie"
sig_bob = bob.signer(msg_bob)

print("\n--- Signature produite par Bob ---")
print("Message signe   :", msg_bob)
print("Signature Bob   :", sig_bob.hex())

print("\n--- Comparaison des signatures ---")
print("Les deux signatures sont identiques ?", sig_alice == sig_bob)

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Quel est le role de la classe Portefeuille ?")
print("-> Elle gere la paire de cles (privee et publique) d'un utilisateur, expose son adresse")
print("   publique et lui permet de signer cryptographiquement ses messages ou transactions.")

print("\nQ2 : Pourquoi chaque portefeuille possede-t-il sa propre paire de cles ?")
print("-> Pour garantir l'independance et l'identite unique de chaque compte dans le systeme.")

print("\nQ3 : Pourquoi la methode signer() utilise-t-elle la cle privee ?")
print("-> Parce que seule la cle privee (secrete) peut generer une signature mathematiquement valide.")

print("\nQ4 : Pourquoi pouvons-nous partager l'adresse du portefeuille ?")
print("-> Parce qu'elle est issue de la cle publique. Partager la cle publique ne permet a personne")
print("   de retrouver la cle privee ni de forger des signatures a notre place.")

print("\nQ5 : Pourquoi ne faut-il pas afficher ou transmettre la cle privee ?")
print("-> Parce que quiconque a acces a la cle privee possede le controle total des fonds du compte.")
