# TP3 - Exercice 4 : Miner une blockchain de trois blocs
# Ahmed Channoufi

import hashlib
import time

class Bloc:
    def __init__(self, index, transaction, previous_hash):
        self.index = index
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculer_hash()

    def calculer_hash(self):
        contenu = (
            str(self.index)
            + "|"
            + self.transaction
            + "|"
            + self.previous_hash
            + "|"
            + str(self.nonce)
        )
        return hashlib.sha256(contenu.encode("utf-8")).hexdigest()

    def miner_bloc(self, difficulte):
        cible = "0" * difficulte
        while not self.hash.startswith(cible):
            self.nonce += 1
            self.hash = self.calculer_hash()

print("=== EXERCICE 4 : Minage d'une blockchain de 3 blocs ===")

difficulte = 3
print(f"Difficulte fixee a : {difficulte} zeros ('000')\n")

# Minage successif des trois blocs
print("Minage du Bloc 1...")
bloc1 = Bloc(1, "Alice envoie 10 euros a Bob", "0")
bloc1.miner_bloc(difficulte)
print(f"-> Bloc 1 mine ! Nonce={bloc1.nonce}, Hash={bloc1.hash}")

print("\nMinage du Bloc 2...")
bloc2 = Bloc(2, "Bob envoie 5 euros a Charlie", bloc1.hash)
bloc2.miner_bloc(difficulte)
print(f"-> Bloc 2 mine ! Nonce={bloc2.nonce}, Hash={bloc2.hash}")

print("\nMinage du Bloc 3...")
bloc3 = Bloc(3, "Charlie envoie 2 euros a Alice", bloc2.hash)
bloc3.miner_bloc(difficulte)
print(f"-> Bloc 3 mine ! Nonce={bloc3.nonce}, Hash={bloc3.hash}")

blockchain = [bloc1, bloc2, bloc3]

# Affichage detaille de la chaine
print("\n" + "=" * 50)
print("ETAT DE LA BLOCKCHAIN APRES MINAGE")
print("=" * 50)
for b in blockchain:
    print("-" * 35)
    print("Bloc           :", b.index)
    print("Transaction    :", b.transaction)
    print("Hash precedent :", b.previous_hash)
    print("Nonce          :", b.nonce)
    print("Hash           :", b.hash)

# Verifications des liaisons
print("\n--- Verifications de coherence ---")
print("Bloc 1 respecte la difficulte ? ", bloc1.hash.startswith("0" * difficulte))
print("Bloc 2 respecte la difficulte ? ", bloc2.hash.startswith("0" * difficulte))
print("Bloc 3 respecte la difficulte ? ", bloc3.hash.startswith("0" * difficulte))
print("Liaison Bloc 1 -> Bloc 2 exacte ?", bloc2.previous_hash == bloc1.hash)
print("Liaison Bloc 2 -> Bloc 3 exacte ?", bloc3.previous_hash == bloc2.hash)

# Reponses aux questions
print("\n=== Reponses aux questions ===")
print("Q1 : Pourquoi doit-on miner le Bloc 1 avant de creer le Bloc 2 ?")
print("-> Parce que le Bloc 2 a besoin du hash DEFINITIF (mine) du Bloc 1 dans son champ previous_hash.")
print("   Tant que le Bloc 1 n'est pas mine, son hash continue de changer a chaque essai de nonce.")

print("\nQ2 : Pourquoi le Bloc 2 depend-il du hash final du Bloc 1 ?")
print("-> Pour etre scelle cryptographiquement au bloc precedent. Si le hash du Bloc 1 changeait")
print("   plus tard, le Bloc 2 deviendrait invalide.")

print("\nQ3 : Les trois blocs possedent-ils necessairement le meme nonce ?")
print("-> Non, chaque bloc a un contenu different (index, texte, previous_hash). Le nombre d'essais")
print("   necessaire pour trouver un hash commencant par '000' est independant et imprevisible.")

print("\nQ4 : Pourquoi le minage d'un bloc depend-il de son contenu ?")
print("-> Parce que le hash est calcule sur l'ensemble des champs concatenes.")
print("   Modifier une lettre de la transaction produit un hash completement different pour un meme nonce.")

print("\nQ5 : Que se passerait-il si nous modifiions une transaction dans le Bloc 1 apres le minage ?")
print("-> Son hash ne commencerait plus par '000' (perte de la preuve de travail), et le lien")
print("   avec le Bloc 2 serait brise (incoherence de previous_hash).")
