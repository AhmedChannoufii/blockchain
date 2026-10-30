# TP4 - Exercice 7 : Construire une blockchain avec plusieurs transactions
# Ahmed Channoufi

import hashlib
import json

class Transaction:
    def __init__(self, expediteur, destinataire, montant):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.montant = montant

    def afficher(self):
        print(f"    {self.expediteur} -> {self.destinataire} : {self.montant} unites")

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

print("=== EXERCICE 7 : Chaine de 3 blocs avec transactions multiples ===")

difficulte = 3

# Bloc 1 (Genesis)
print("Minage du Bloc 1...")
tx1 = [
    Transaction("Alice", "Bob", 20),
    Transaction("Bob", "Charlie", 10)
]
bloc1 = Bloc(1, tx1, "0")
bloc1.miner_bloc(difficulte)

# Bloc 2
print("Minage du Bloc 2...")
tx2 = [
    Transaction("Charlie", "David", 5),
    Transaction("David", "Alice", 2)
]
bloc2 = Bloc(2, tx2, bloc1.hash)
bloc2.miner_bloc(difficulte)

# Bloc 3 (demande dans le travail a faire)
print("Minage du Bloc 3...")
tx3 = [
    Transaction("Alice", "Charlie", 15),
    Transaction("Charlie", "Bob", 8)
]
bloc3 = Bloc(3, tx3, bloc2.hash)
bloc3.miner_bloc(difficulte)

blockchain = [bloc1, bloc2, bloc3]

# Affichage de la blockchain
print("\n" + "=" * 55)
print("ETAT DE LA BLOCKCHAIN COMPLETE (3 BLOCS)")
print("=" * 55)
for b in blockchain:
    print("-" * 45)
    print("Bloc           :", b.index)
    print("Hash precedent :", b.previous_hash)
    print("Hash actuel    :", b.hash)
    print("Nonce          :", b.nonce)
    print("Transactions   :")
    for t in b.transactions:
        t.afficher()

# Verification des liens
print("\n--- Verification du chainage ---")
print("Liaison Bloc 1 -> Bloc 2 exacte ?", bloc2.previous_hash == bloc1.hash)
print("Liaison Bloc 2 -> Bloc 3 exacte ?", bloc3.previous_hash == bloc2.hash)

# Test de falsification du bloc 1 apres minage
print("\n--- Test de falsification sur le Bloc 1 apres minage ---")
hash_enregistre = bloc1.hash
print("Hash enregistre dans le Bloc 1 :", hash_enregistre)

# Un attaquant modifie en memoire la 1ere transaction (20 -> 200 unites)
bloc1.transactions[0].montant = 200
hash_recalcule = bloc1.calculer_hash()
print("Hash recalcule apres modif     :", hash_recalcule)
print("L'integrite du Bloc 1 est violee ?", hash_enregistre != hash_recalcule)
print("Le hash recalcule commence encore par '000' ?", hash_recalcule.startswith("0" * difficulte))
print("Le Bloc 2 pointe-t-il vers le nouveau hash du Bloc 1 ?", bloc2.previous_hash == hash_recalcule)

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Pourquoi devons-nous miner le premier bloc avant de construire le deuxieme ?")
print("-> Parce que le deuxieme bloc a besoin du hash definitif du premier dans previous_hash.")
print("   Tant que le premier bloc n'est pas termine de miner, son hash change a chaque essai de nonce.")

print("\nQ2 : Pourquoi le deuxieme bloc contient-il le hash du premier ?")
print("-> Pour creer un lien cryptographique inviolable garantissant l'ordre et l'integrite de l'historique.")

print("\nQ3 : Comment les transactions influencent-elles le hash d'un bloc ?")
print("-> Elles sont serialisees en json dans le contenu du bloc. La moindre modification d'un montant")
print("   ou d'un nom entraine un hash completement different (effet avalanche).")

print("\nQ4 : Pourquoi une modification du premier bloc peut-elle affecter les blocs suivants ?")
print("-> Changer le bloc 1 change son hash, ce qui brise le previous_hash du bloc 2,")
print("   qui a son tour change de hash et brise le bloc 3 (effet en cascade).")

print("\nQ5 : Notre programme verifie-t-il automatiquement les soldes avant d'ajouter les transactions aux blocs ?")
print("-> Non. Dans cet exercice, nous avons instancie directement la classe Bloc avec une liste arbitraire.")
print("   Pour securiser la blockchain, il faut combiner le validateur de l'exercice 4 avant d'inserer")
print("   les transactions dans le bloc.")
