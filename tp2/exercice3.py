# TP2 - Exercice 3 : Construire une blockchain de trois blocs
# Ahmed Channoufi

import hashlib

print("=== EXERCICE 3 : Chaine de trois blocs ===")

# Classe Bloc
class Bloc:
    def __init__(self, index, transaction, previous_hash):
        self.index = index
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.hash = self.calculer_hash()

    def calculer_hash(self):
        contenu = str(self.index) + "|" + self.transaction + "|" + self.previous_hash
        return hashlib.sha256(contenu.encode("utf-8")).hexdigest()

# Creation des trois blocs lies
# Bloc 1 (genesis) : n'a pas de predecesseur donc previous_hash = "0"
bloc1 = Bloc(1, "Alice envoie 10 euros a Bob", "0")

# Bloc 2 : prend le hash du bloc 1
bloc2 = Bloc(2, "Bob envoie 5 euros a Charlie", bloc1.hash)

# Bloc 3 : prend le hash du bloc 2
bloc3 = Bloc(3, "Charlie envoie 2 euros a Alice", bloc2.hash)

# On regroupe les blocs dans une liste
blockchain = [bloc1, bloc2, bloc3]

# Affichage des blocs
print("\n--- Contenu de la blockchain ---")
for bloc in blockchain:
    print("-" * 30)
    print("Bloc           :", bloc.index)
    print("Transaction    :", bloc.transaction)
    print("Hash precedent :", bloc.previous_hash)
    print("Hash actuel    :", bloc.hash)

# Verification du chainage
print("\n--- Verification des liaisons ---")
print("Le previous_hash du bloc 2 correspond au hash du bloc 1 ?", bloc2.previous_hash == bloc1.hash)
print("Le previous_hash du bloc 3 correspond au hash du bloc 2 ?", bloc3.previous_hash == bloc2.hash)

# Reponses aux questions
print("\n=== Reponses aux questions ===")
print("Q1 : Comment les blocs sont-ils relies entre eux ?")
print("-> Chaque bloc stocke dans son attribut 'previous_hash' l'empreinte numerique (hash)")
print("   du bloc qui le precede directement.")

print("\nQ2 : Pourquoi le Bloc 2 utilise-t-il bloc1.hash ?")
print("-> Pour creer un lien cryptographique inviolable avec le premier bloc.")

print("\nQ3 : Pourquoi le Bloc 3 utilise-t-il bloc2.hash ?")
print("-> C'est le principe de la chaine : chaque nouveau bloc fait reference au precedent.")

print("\nQ4 : Quel est le role de la liste 'blockchain' ?")
print("-> Elle permet de stocker l'ensemble des blocs de facon ordonnee dans notre programme.")

print("\nQ5 : Que se passerait-il si on mettait '12345' a la place de bloc1.hash pour le Bloc 2 ?")
print("-> Le lien serait faux car '12345' n'est pas le vrai hash du Bloc 1.")
print("   La chaine serait alors consideree comme corrompue.")
