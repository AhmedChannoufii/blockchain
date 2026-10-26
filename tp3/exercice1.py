# TP3 - Exercice 1 : Recherche d'un hash commencant par des zeros (Proof of Work)
# Ahmed Channoufi

import hashlib

def miner_texte(message, cible="000"):
    nonce = 0
    while True:
        contenu = message + str(nonce)
        hash_resultat = hashlib.sha256(contenu.encode("utf-8")).hexdigest()
        if hash_resultat.startswith(cible):
            break
        nonce += 1
    return nonce, hash_resultat

print("=== EXERCICE 1 : Recherche d'un hash avec '000' ===")

# Test 1 : avec le message "Blockchain"
message1 = "Blockchain"
nonce1, hash1 = miner_texte(message1)

print("\n--- Test 1 : Message = 'Blockchain' ---")
print("Message :", message1)
print("Nonce   :", nonce1)
print("Hash    :", hash1)
print("Verif   : Le hash commence bien par '000' ?", hash1.startswith("000"))

# Test 2 : avec le message "Bitcoin"
message2 = "Bitcoin"
nonce2, hash2 = miner_texte(message2)

print("\n--- Test 2 : Message = 'Bitcoin' ---")
print("Message :", message2)
print("Nonce   :", nonce2)
print("Hash    :", hash2)
print("Verif   : Le hash commence bien par '000' ?", hash2.startswith("000"))

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Quel est le role de la variable nonce ?")
print("-> C'est un compteur numerique arbitraire ('number used once') qu'on incremente")
print("   a chaque tentative afin de modifier l'entree du hash sans toucher au message initial.")

print("\nQ2 : Pourquoi utilisons-nous une boucle while ?")
print("-> Parce qu'on ne sait pas a l'avance combien de tentatives seront necessaires")
print("   pour trouver un hash valide. La boucle continue jusqu'a ce que la condition soit verifiee.")

print("\nQ3 : Quel est le role de la methode startswith() ?")
print("-> Elle verifie si la chaine de caracteres du hash debute par le motif demande (ici '000').")

print("\nQ4 : Pourquoi le programme effectue-t-il plusieurs calculs ?")
print("-> Les fonctions de hachage etant pseudo-aleatoires (effet avalanche), il est impossible")
print("   de predire quel nonce donnera un hash commencant par '000'. Il faut donc essayer par force brute.")

print("\nQ5 : Le meme message produit-il toujours le meme nonce dans ce programme ? Justifiez.")
print("-> Oui, car SHA-256 est une fonction deterministe. A chaque execution sur le meme message")
print("   en partant de nonce=0, on testera les memes valeurs dans le meme ordre et on obtiendra le meme nonce.")

print("\nQ6 : Pourquoi la modification du message peut-elle changer le nonce trouve ?")
print("-> Changer ne serait-ce qu'une lettre modifie totalement la suite des empreintes produites.")
print("   Pour 'Bitcoin', la premiere valeur donnant '000' n'apparait pas du tout a la meme tentative.")
