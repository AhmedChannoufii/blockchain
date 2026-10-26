# TP3 - Exercice 3 : Ajouter le minage a la classe Bloc
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
        # On inclut desormais self.nonce dans le contenu hache
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
        debut = time.perf_counter()
        
        while not self.hash.startswith(cible):
            self.nonce += 1
            self.hash = self.calculer_hash()
            
        fin = time.perf_counter()
        duree = fin - debut
        
        print(f"Bloc {self.index} mine avec succes !")
        print(f"  Difficulte     : {difficulte}")
        print(f"  Nonce trouve   : {self.nonce}")
        print(f"  Hash valide    : {self.hash}")
        print(f"  Temps de calcul: {duree:.6f} s")
        return duree

print("=== EXERCICE 3 : Classe Bloc avec Proof of Work ===")

# Test 1 : Difficulte = 3
print("\n--- Test 1 : Minage avec difficulte = 3 ---")
bloc1 = Bloc(1, "Alice envoie 10 euros a Bob", "0")
print("Hash initial (avant minage, nonce=0) :", bloc1.hash)
bloc1.miner_bloc(3)

# Test 2 : Difficulte = 4 (sur une nouvelle instance pour comparaison)
print("\n--- Test 2 : Minage avec difficulte = 4 ---")
bloc1_diff4 = Bloc(1, "Alice envoie 10 euros a Bob", "0")
bloc1_diff4.miner_bloc(4)

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Quelle difference existe-t-il entre cette classe et celle du TP2 ?")
print("-> Deux ajouts majeurs :")
print("   1. L'attribut 'nonce', inclus dans le calcul du hash.")
print("   2. La methode 'miner_bloc(difficulte)' qui boucle jusqu'a obtenir un hash conforme.")

print("\nQ2 : Pourquoi avons-nous ajoute l'attribut nonce ?")
print("-> Pour pouvoir changer l'empreinte du bloc sans toucher a ses donnees metier")
print("   (transactions, index, hash precedent). Le nonce est la seule variable libre.")

print("\nQ3 : Quel est le role de la methode miner_bloc() ?")
print("-> Elle implemente l'algorithme de Proof of Work : elle incremente le nonce et recalcule")
print("   le hash tant que ce dernier ne commence pas par le nombre de zeros requis.")

print("\nQ4 : Pourquoi le hash est-il recalcule a chaque modification du nonce ?")
print("-> Parce que SHA-256 depend de chaque bit en entree. Des que le nonce change,")
print("   l'empreinte devient completement differente ; il faut verifier si elle respecte la cible.")

print("\nQ5 : Pourquoi le minage s'arrete-t-il lorsqu'un hash valide est trouve ?")
print("-> Parce que la preuve de travail est atteinte (condition de sortie de la boucle).")
print("   Le bloc est pret a etre accepte et scelle dans la blockchain.")
