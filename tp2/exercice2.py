# TP2 - Exercice 2 : Creer son premier bloc
# Ahmed Channoufi

import hashlib

print("=== EXERCICE 2 : Creation d'un premier bloc ===")

# Definition de la classe Bloc
class Bloc:
    def __init__(self, index, transaction, previous_hash):
        self.index = index
        self.transaction = transaction
        self.previous_hash = previous_hash
        # Calcul automatique du hash a la creation
        self.hash = self.calculer_hash()

    def calculer_hash(self):
        # On concatene les donnees du bloc sous forme de chaine
        contenu = str(self.index) + "|" + self.transaction + "|" + self.previous_hash
        return hashlib.sha256(contenu.encode("utf-8")).hexdigest()

# Creation du premier bloc (bloc genesis)
bloc1 = Bloc(1, "Alice envoie 10 euros a Bob", "0")

print("\n--- Informations du Bloc 1 ---")
print("Index           :", bloc1.index)
print("Transaction     :", bloc1.transaction)
print("Hash precedent  :", bloc1.previous_hash)
print("Hash actuel     :", bloc1.hash)

# Test de modification : on change 10 euros en 100 euros
print("\n--- Test de modification de la transaction ---")
bloc1_modifie = Bloc(1, "Alice envoie 100 euros a Bob", "0")
print("Hash original :", bloc1.hash)
print("Hash modifie  :", bloc1_modifie.hash)
print("Les deux hash sont identiques ?", bloc1.hash == bloc1_modifie.hash)

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Quel est le role de la methode __init__() ?")
print("-> C'est le constructeur de la classe en Python. Il est execute automatiquement")
print("   lorsqu'on instancie un nouvel objet Bloc pour initialiser ses attributs.")

print("\nQ2 : Quel est le role de la ligne 'self.hash = self.calculer_hash()' ?")
print("-> Elle permet de calculer et d'enregistrer l'empreinte numerique du bloc")
print("   automatiquement des sa creation.")

print("\nQ3 : Pourquoi convertit-on index en chaine avec str(self.index) ?")
print("-> Parce que l'index est un entier (int). Pour pouvoir le concatener avec")
print("   les autres chaines de caracteres et l'encoder en utf-8, il faut le convertir en texte.")

print("\nQ4 : Quels sont les attributs utilises pour calculer le hash du bloc ?")
print("-> L'index, la transaction et le previous_hash.")

print("\nQ5 : Que constate-t-on apres modification de la transaction ?")
print("-> Le hash du bloc change completement, meme en ne modifiant qu'un seul chiffre.")
