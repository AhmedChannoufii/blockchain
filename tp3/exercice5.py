# TP3 - Exercice 5 : Verifier une blockchain avec Proof of Work
# Ahmed Channoufi

import hashlib

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

# Fonction complete de verification
def verifier_blockchain(blockchain, difficulte):
    cible = "0" * difficulte
    for i in range(len(blockchain)):
        bloc = blockchain[i]

        # 1. Verification du contenu (integrite interne du bloc)
        if bloc.hash != bloc.calculer_hash():
            print(f"  [ECHEC] Bloc {bloc.index} : contenu altere ! (hash stocke != hash calcule)")
            return False

        # 2. Verification de la preuve de travail (Proof of Work)
        if not bloc.hash.startswith(cible):
            print(f"  [ECHEC] Bloc {bloc.index} : preuve de travail invalide ! (ne commence pas par {cible})")
            return False

        # 3. Verification du chainage cryptographique
        if i > 0:
            bloc_precedent = blockchain[i - 1]
            if bloc.previous_hash != bloc_precedent.hash:
                print(f"  [ECHEC] Bloc {bloc.index} : lien brise ! (previous_hash != hash du bloc {bloc_precedent.index})")
                return False

    return True

print("=== EXERCICE 5 : Verification d'une blockchain PoW ===")

difficulte = 3

# Creation et minage de la chaine initiale
print("Minage initial de la blockchain (difficulte = 3)...")
bloc1 = Bloc(1, "Alice envoie 10 euros a Bob", "0")
bloc1.miner_bloc(difficulte)

bloc2 = Bloc(2, "Bob envoie 5 euros a Charlie", bloc1.hash)
bloc2.miner_bloc(difficulte)

bloc3 = Bloc(3, "Charlie envoie 2 euros a Alice", bloc2.hash)
bloc3.miner_bloc(difficulte)

blockchain = [bloc1, bloc2, bloc3]
print("Minage termine !\n")

# Test 1 : Verification de la chaine intacte
print("--- Test 1 : Verification de la blockchain originale ---")
valide = verifier_blockchain(blockchain, difficulte)
print("Resultat de la verification :", valide)

# Test 2 : Modification frauduleuse d'une transaction
print("\n--- Test 2 : Falsification de la transaction du Bloc 1 ---")
print("Tentative de piratage : Alice envoie 1000 euros a Bob (sans reminer)")
bloc1.transaction = "Alice envoie 1000 euros a Bob"
valide_apres = verifier_blockchain(blockchain, difficulte)
print("Resultat de la verification :", valide_apres)

# Reponses aux questions
print("\n=== Reponses aux questions ===")
print("Q1 : Pourquoi verifions-nous le hash du bloc ?")
print("-> Pour controler que le contenu stocke (transaction, index, nonce) n'a pas ete modifie.")
print("   Si le texte change sans mettre a jour le hash, l'incoherence apparait des le premier test.")

print("\nQ2 : Pourquoi verifions-nous le nombre de zeros au debut du hash ?")
print("-> Pour valider que le bloc a reellement respecte la difficulte de calcul requise.")
print("   Si un attaquant change le texte et recalcule un hash quelconque (sans miner), il sera rejete.")

print("\nQ3 : Pourquoi verifions-nous le hash du bloc precedent ?")
print("-> Pour garantir l'ordre et la continuite de la chaine. Aucun bloc ne peut etre permute ou remplace.")

print("\nQ4 : Quelle est la difference entre cette fonction et celle developpee dans le TP2 ?")
print("-> Dans le TP2, on verifiait seulement l'integrite du texte et le chainage.")
print("   Ici, on a ajoute la verification du Proof of Work (bloc.hash.startswith(cible)).")

print("\nQ5 : Le Proof of Work empeche-t-il totalement la modification d'une blockchain ? Justifiez.")
print("-> Non, pas mathematiquement de maniere absolue. Un attaquant qui possede plus de 51% de la")
print("   puissance de calcul du reseau pourrait theoretiquement re-miner une chaine plus longue.")
print("   En revanche, pour un acteur isole, cela rend la fraude economiquement et techniquement infaisable.")
