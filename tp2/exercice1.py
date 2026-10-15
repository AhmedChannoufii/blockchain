# TP2 - Exercice 1 : Decouverte de SHA-256
# Ahmed Channoufi

import hashlib

print("=== EXERCICE 1 : Decouverte de la fonction SHA-256 ===")

# Etape 2 : Calcul d'un premier hash
texte = "Blockchain"
hash_texte = hashlib.sha256(texte.encode("utf-8")).hexdigest()

print("Texte :", texte)
print("Hash  :", hash_texte)

# Etape 3 : Tests avec d'autres chaines
print("\n--- Tests et comparaisons ---")

# 1. En minuscules
texte2 = "blockchain"
hash2 = hashlib.sha256(texte2.encode("utf-8")).hexdigest()
print("Texte :", texte2)
print("Hash  :", hash2)

# 2. Texte plus long
texte3 = "Blockchain et cryptographie"
hash3 = hashlib.sha256(texte3.encode("utf-8")).hexdigest()
print("Texte :", texte3)
print("Hash  :", hash3)

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Deux textes differents donnent-ils le meme hash ?")
print("-> Non, 'Blockchain' et 'blockchain' donnent des hashs totalement differents.")
print("   Une simple majuscule modifie completement le resultat (effet avalanche).")

print(f"\nQ2 : Quelle est la longueur du hash SHA-256 en caracteres ?")
print(f"-> Le hash fait {len(hash_texte)} caracteres hexadecimaux (soit 256 bits).")

print("\nQ3 : La longueur du texte d'origine change-t-elle la longueur du hash ?")
print("-> Non, quelle que soit la taille de la chaine, le hash fait toujours 64 caracteres.")

print("\nQ4 : Pourquoi le hachage est-il utile dans la blockchain ?")
print("-> Il sert d'empreinte numerique unique pour chaque bloc. Si le contenu change,")
print("   le hash change aussi, ce qui permet de detecter la moindre modification.")

print("\nQ5 : Peut-on retrouver facilement le texte initial a partir du hash ?")
print("-> Non, SHA-256 est une fonction a sens unique. On ne peut pas faire l'operation inverse.")
