# TP2 - Exercice 5 : Ajouter un quatrieme bloc
# Ahmed Channoufi

import hashlib

print("=== EXERCICE 5 : Ajout d'un 4eme bloc ===")

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

# Fonction de verification
def verifier_blockchain(chaine):
    for i in range(len(chaine)):
        bloc = chaine[i]
        if bloc.hash != bloc.calculer_hash():
            return False
        if i > 0 and bloc.previous_hash != chaine[i - 1].hash:
            return False
    return True

# Creation des 3 premiers blocs
bloc1 = Bloc(1, "Alice envoie 10 euros a Bob", "0")
bloc2 = Bloc(2, "Bob envoie 5 euros a Charlie", bloc1.hash)
bloc3 = Bloc(3, "Charlie envoie 2 euros a Alice", bloc2.hash)

# Ajout du quatrieme bloc
# Son previous_hash doit obligatoirement etre le hash du bloc 3
bloc4 = Bloc(4, "David envoie 15 euros a Alice", bloc3.hash)

# Assemblage de la blockchain complete
blockchain = [bloc1, bloc2, bloc3, bloc4]

# Affichage des 4 blocs
print("\n--- Blockchain a 4 blocs ---")
for b in blockchain:
    print("-" * 30)
    print("Bloc           :", b.index)
    print("Transaction    :", b.transaction)
    print("Hash precedent :", b.previous_hash)
    print("Hash actuel    :", b.hash)

# Verification de la chaine
valide = verifier_blockchain(blockchain)
print("\nVerification de la chaine complete :", valide)

# Reponses aux questions
print("\n=== Reponses aux questions ===")
print("Q1 : Quel hash doit etre utilise comme hash precedent du Bloc 4 ?")
print(f"-> Le hash du Bloc 3 (bloc3.hash) : {bloc3.hash}")

print("\nQ2 : Pourquoi ne pas utiliser le hash du Bloc 1 ?")
print("-> Parce que la blockchain est chronologique et lineaire. Chaque bloc doit")
print("   s'accrocher au bloc qui le precede directement (Bloc 3).")

print("\nQ3 : Que se passe-t-il si le Bloc 4 a un mauvais hash precedent ?")
bloc4_faux = Bloc(4, "David envoie 15 euros a Alice", "FAUX_HASH_123")
chaine_fausse = [bloc1, bloc2, bloc3, bloc4_faux]
print("-> Resultat du test avec un faux hash :", verifier_blockchain(chaine_fausse))
print("   La fonction renvoie False car le lien entre le bloc 3 et le bloc 4 est rompu.")
