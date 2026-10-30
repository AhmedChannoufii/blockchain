# TP5 - Exercice 1 : Generer une paire de cles cryptographiques
# Ahmed Channoufi

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

print("=== EXERCICE 1 : Generation d'une paire de cles Ed25519 ===")

# Generation de la cle privee
cle_privee = Ed25519PrivateKey.generate()

# Recuperation de la cle publique correspondante
cle_publique = cle_privee.public_key()

# Conversion de la cle publique en octets bruts
cle_publique_bytes = cle_publique.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)

print("\n--- Cle publique generee ---")
print("Cle publique (hex) :", cle_publique_bytes.hex())
print("Longueur en octets :", len(cle_publique_bytes), "octets")
print("Longueur en hex    :", len(cle_publique_bytes.hex()), "caracteres")

# Test d'une deuxieme generation pour comparer
cle_privee_2 = Ed25519PrivateKey.generate()
cle_publique_2_bytes = cle_privee_2.public_key().public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)
print("\n--- Deuxieme generation (pour comparaison) ---")
print("Nouvelle cle (hex) :", cle_publique_2_bytes.hex())
print("Les deux cles sont identiques ?", cle_publique_bytes == cle_publique_2_bytes)

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Pourquoi generons-nous deux cles differentes ?")
print("-> C'est le principe de la cryptographie asymetrique : une cle sert a signer (la cle privee)")
print("   et l'autre sert a verifier la signature (la cle publique).")

print("\nQ2 : Quel est le role de la cle privee ?")
print("-> Elle permet a son proprietaire de produire des signatures numeriques prouvant son consentement.")

print("\nQ3 : Quel est le role de la cle publique ?")
print("-> Elle est partagee avec tout le monde pour permettre a n'importe quel participant de verifier")
print("   l'authenticite des signatures emises par la cle privee correspondante.")

print("\nQ4 : Pourquoi la cle privee doit-elle rester secrete ?")
print("-> Parce que quiconque possede la cle privee peut emettre des signatures valides et vider les fonds")
print("   du compte en se faisant passer pour son proprietaire (usurpation d'identite).")

print("\nQ5 : Pourquoi les cles changent-elles lors de nouvelles generations ?")
print("-> Parce que la generation utilise de l'entropie aleatoire securisee (nombres aleatoires cryptographiques)")
print("   pour garantir que chaque utilisateur recoit une paire de cles unique au monde et imprevisible.")
