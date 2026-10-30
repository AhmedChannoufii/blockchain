# TP4 - Exercice 6 : Creer un bloc contenant plusieurs transactions
# Ahmed Channoufi

import hashlib
import json

class Transaction:
    def __init__(self, expediteur, destinataire, montant):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.montant = montant

    def afficher(self):
        print(f"  {self.expediteur} -> {self.destinataire} : {self.montant} unites")

class Bloc:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculer_hash()

    def calculer_hash(self):
        contenu = {
            "index": self.index,
            "transactions": [
                {
                    "expediteur": t.expediteur,
                    "destinataire": t.destinataire,
                    "montant": t.montant
                }
                for t in self.transactions
            ],
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }
        texte = json.dumps(
            contenu,
            sort_keys=True,
            separators=(",", ":")
        )
        return hashlib.sha256(texte.encode("utf-8")).hexdigest()

    def miner_bloc(self, difficulte):
        cible = "0" * difficulte
        while not self.hash.startswith(cible):
            self.nonce += 1
            self.hash = self.calculer_hash()

print("=== EXERCICE 6 : Bloc multi-transactions ===")

# Test 1 : Bloc initial a 3 transactions (difficulte 3)
transactions1 = [
    Transaction("Alice", "Bob", 20),
    Transaction("Bob", "Charlie", 10),
    Transaction("Charlie", "David", 5)
]

bloc1 = Bloc(1, transactions1, "0")
print("Minage du Bloc 1 (3 transactions, difficulte 3)...")
bloc1.miner_bloc(3)

print("--- Informations du Bloc 1 ---")
print("Index                  :", bloc1.index)
print("Nombre de transactions :", len(bloc1.transactions))
print("Nonce                  :", bloc1.nonce)
print("Hash                   :", bloc1.hash)
print("Transactions incluses  :")
for t in bloc1.transactions:
    t.afficher()

# Test 2 : Modification d'un montant (effet sur le hash)
transactions2 = [
    Transaction("Alice", "Bob", 50), # montant modifie (20 -> 50)
    Transaction("Bob", "Charlie", 10),
    Transaction("Charlie", "David", 5)
]
bloc1_modifie = Bloc(1, transactions2, "0")
print("\n--- Test apres modification de la transaction 1 (20 -> 50) avant minage ---")
print("Hash initial (nonce=0) original :", Bloc(1, transactions1, "0").hash)
print("Hash initial (nonce=0) modifie  :", bloc1_modifie.hash)
bloc1_modifie.miner_bloc(3)
print("Nouveau nonce trouve :", bloc1_modifie.nonce)
print("Nouveau hash mine    :", bloc1_modifie.hash)

# Test 3 : Ajout d'une 4eme transaction
transactions3 = [
    Transaction("Alice", "Bob", 20),
    Transaction("Bob", "Charlie", 10),
    Transaction("Charlie", "David", 5),
    Transaction("David", "Alice", 2) # 4eme transaction ajoutee
]
bloc1_4tx = Bloc(1, transactions3, "0")
print("\n--- Minage avec 4 transactions ---")
bloc1_4tx.miner_bloc(3)
print("Nonce avec 4 transactions :", bloc1_4tx.nonce)
print("Hash avec 4 transactions  :", bloc1_4tx.hash)

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Pourquoi utilisons-nous une liste de transactions ?")
print("-> Pour pouvoir grouper et enregistrer plusieurs operations financieres dans un meme bloc.")

print("\nQ2 : Quel est le role de la bibliotheque json ?")
print("-> Elle permet de convertir le dictionnaire d'objets en une chaine de texte standardisee (json.dumps).")

print("\nQ3 : Pourquoi devons-nous convertir les informations du bloc en texte avant de calculer le hash ?")
print("-> Parce que hashlib.sha256 prend des octets en entree (bytes). Il faut d'abord serialiser en texte")
print("   avec sort_keys=True pour que l'ordre des cles soit toujours deterministe.")

print("\nQ4 : Pourquoi le hash depend-il de toutes les transactions ?")
print("-> Parce que la liste complete des transactions est serialisee dans le json hache.")
print("   La moindre modification d'un expediteur, destinataire ou montant change le texte et donc le hash.")

print("\nQ5 : Que se passe-t-il si une transaction est modifiee apres le minage ?")
print("-> Le hash calcule a partir du contenu devient different du hash stocke, et la condition")
print("   de Proof of Work (les 3 zeros) est perdue. Le bloc est invalide.")

print("\nQ6 : Pourquoi le nonce intervient-il dans le calcul du hash ?")
print("-> Parce que c'est la seule variable libre que le mineur peut incrementer pour explorer")
print("   l'espace des hashs sans modifier le contenu des transactions.")
