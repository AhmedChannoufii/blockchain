# TP5 - Exercice 2 : Signer un message avec une cle privee
# Ahmed Channoufi

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

print("=== EXERCICE 2 : Signature d'un message avec Ed25519 ===")

# Generation d'une paire de cles
cle_privee = Ed25519PrivateKey.generate()
cle_publique = cle_privee.public_key()

# Message 1
message1 = "Alice envoie 20 unites a Bob"
message1_bytes = message1.encode("utf-8")
signature1 = cle_privee.sign(message1_bytes)

print("\n--- Test 1 : Signature du message original ---")
print("Message 1          :", message1)
print("Signature 1 (hex)  :", signature1.hex())
print("Longueur signature :", len(signature1), "octets (soit", len(signature1.hex()), "caracteres hex)")

# Message 2 (montant modifie : 20 -> 50)
message2 = "Alice envoie 50 unites a Bob"
message2_bytes = message2.encode("utf-8")
signature2 = cle_privee.sign(message2_bytes)

print("\n--- Test 2 : Signature apres modification (20 -> 50) ---")
print("Message 2          :", message2)
print("Signature 2 (hex)  :", signature2.hex())
print("Les deux signatures sont identiques ?", signature1 == signature2)

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Quelle cle est utilisee pour signer le message ?")
print("-> La cle privee (cle_privee).")

print("\nQ2 : Pourquoi convertissons-nous le message en octets ?")
print("-> Les primitives cryptographiques (Ed25519) manipulent des flux binaires d'octets (bytes),")
print("   donc il faut encoder la chaine str avec encode('utf-8').")

print("\nQ3 : Quel est le role de la methode sign() ?")
print("-> Elle calcule une signature numerique cryptographique a partir du message et de la cle privee.")

print("\nQ4 : Une signature numerique est-elle identique a un hash ?")
print("-> Non. Un hash depend uniquement du message et peut etre recalcule par n'importe qui.")
print("   Une signature depend a la fois du message ET du secret de la cle privee.")

print("\nQ5 : Pourquoi la signature depend-elle du message ?")
print("-> Pour lier indissociablement l'approbation de l'expediteur a ce contenu precis.")
print("   Si le message change ne serait-ce que d'un chiffre, la signature initiale ne correspond plus.")
