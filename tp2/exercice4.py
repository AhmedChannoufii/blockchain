# TP2 - Exercice 4 : Verifier l'integrite de la blockchain
# Ahmed Channoufi

import hashlib

print("=== EXERCICE 4 : Verification de l'integrite ===")

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

# Construction de la blockchain de base
bloc1 = Bloc(1, "Alice envoie 10 euros a Bob", "0")
bloc2 = Bloc(2, "Bob envoie 5 euros a Charlie", bloc1.hash)
bloc3 = Bloc(3, "Charlie envoie 2 euros a Alice", bloc2.hash)
blockchain = [bloc1, bloc2, bloc3]

# Fonction de verification
def verifier_blockchain(chaine):
    for i in range(len(chaine)):
        bloc = chaine[i]

        # 1. Verification du contenu du bloc
        if bloc.hash != bloc.calculer_hash():
            print(f"[ERREUR] Bloc {bloc.index} : le contenu a ete modifie !")
            return False

        # 2. Verification du lien avec le bloc precedent
        if i > 0:
            bloc_prec = chaine[i - 1]
            if bloc.previous_hash != bloc_prec.hash:
                print(f"[ERREUR] Bloc {bloc.index} : lien brise avec le bloc precedent !")
                return False

    return True

# Test 1 : Verification de la blockchain intacte
print("\n--- Test sur la chaine valide ---")
est_valide = verifier_blockchain(blockchain)
print("Resultat de verification :", est_valide)

# Test 2 : Falsification d'une transaction sans recalculer le hash
print("\n--- Test apres modification frauduleuse du Bloc 1 ---")
bloc1.transaction = "Alice envoie 1000 euros a Bob"
est_valide_apres = verifier_blockchain(blockchain)
print("Resultat de verification :", est_valide_apres)

# Reponses aux questions
print("\n=== Reponses aux questions ===")
print("Q1 : Pourquoi doit-on recalculer le hash pour verifier un bloc ?")
print("-> Pour verifier que les donnees actuelles correspondent bien au hash enregistre.")
print("   Si quelqu'un a modifie le texte en memoire, le nouveau hash sera different.")

print("\nQ2 : Pourquoi la verification du 'previous_hash' est-elle indispensable ?")
print("-> Pour garantir que la chaine n'a pas ete brisee et que l'ordre des blocs")
print("   est respecte.")

print("\nQ3 : Quelle est la difference entre verifier le contenu et verifier la liaison ?")
print("-> Verifier le contenu controle l'integrite interne du bloc (hash vs hash calcule).")
print("   Verifier la liaison controle que le bloc pointe bien vers le hash du precedent.")

print("\nQ4 : Cette fonction suffit-elle a securiser une vraie blockchain ?")
print("-> Non. Sur un seul ordinateur, quelqu'un pourrait recalculer tous les hashs")
print("   a la suite. Une vraie blockchain a besoin d'un reseau de pairs (P2P),")
print("   de signatures cryptographiques et d'un consensus (comme le Proof of Work).")
