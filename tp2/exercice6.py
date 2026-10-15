# TP2 - Exercice 6 : Experimentations et falsification
# Ahmed Channoufi

import hashlib

print("=== EXERCICE 6 : Tests de falsification et partie comprehension ===")

# Definition de la classe Bloc
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
        # Verif 1 : integrite du contenu
        if bloc.hash != bloc.calculer_hash():
            return False
        # Verif 2 : liaison avec le bloc d'avant
        if i > 0 and bloc.previous_hash != chaine[i - 1].hash:
            return False
    return True

# Fonction utilitaire pour recreer une chaine propre de 4 blocs
def creer_chaine():
    b1 = Bloc(1, "Alice envoie 10 euros a Bob", "0")
    b2 = Bloc(2, "Bob envoie 5 euros a Charlie", b1.hash)
    b3 = Bloc(3, "Charlie envoie 2 euros a Alice", b2.hash)
    b4 = Bloc(4, "David envoie 15 euros a Alice", b3.hash)
    return [b1, b2, b3, b4]

# --- Manipulation 1 ---
print("\n--- Manipulation 1 : Modifier la transaction du bloc 2 sans recalculer son hash ---")
chaine1 = creer_chaine()
chaine1[1].transaction = "Bob envoie 999 euros a Charlie"
res1 = verifier_blockchain(chaine1)
print("Resultat de la verification :", res1)
print("-> Invalide car le hash enregistre ne correspond plus au texte modifie.")

# --- Manipulation 2 ---
print("\n--- Manipulation 2 : Modifier le previous_hash du bloc 3 ---")
chaine2 = creer_chaine()
chaine2[2].previous_hash = "00000000000000000000"
res2 = verifier_blockchain(chaine2)
print("Resultat de la verification :", res2)
print("-> Invalide car le lien avec le bloc 2 est coupe.")

# --- Manipulation 3 ---
print("\n--- Manipulation 3 : Ajouter correctement un 5eme bloc ---")
chaine3 = creer_chaine()
b5 = Bloc(5, "Eve envoie 7 euros a David", chaine3[-1].hash)
chaine3.append(b5)
res3 = verifier_blockchain(chaine3)
print("Resultat de la verification :", res3)
print("-> Valide car le 5eme bloc a bien pris le hash du bloc 4.")

# --- Manipulation 4 ---
print("\n--- Manipulation 4 : Modifier le bloc 1 et recalculer SEULEMENT son hash ---")
chaine4 = creer_chaine()
chaine4[0].transaction = "Alice envoie 500 euros a Bob"
chaine4[0].hash = chaine4[0].calculer_hash()
res4 = verifier_blockchain(chaine4)
print("Resultat de la verification :", res4)
print("-> Invalide car le bloc 2 contient encore l'ancien hash du bloc 1.")

# --- Manipulation 5 ---
print("\n--- Manipulation 5 : Modifier le bloc 1 et recalculer TOUS les hashs suivants ---")
chaine5 = creer_chaine()
chaine5[0].transaction = "Alice envoie 500 euros a Bob"
chaine5[0].hash = chaine5[0].calculer_hash()

# On recalcule en cascade
for i in range(1, len(chaine5)):
    chaine5[i].previous_hash = chaine5[i - 1].hash
    chaine5[i].hash = chaine5[i].calculer_hash()

res5 = verifier_blockchain(chaine5)
print("Resultat de la verification locale :", res5)
print("-> En local, la fonction renvoie True car tous les liens ont ete mis a jour.")
print("   MAIS sur un vrai reseau, cette chaine serait rejetee par les autres noeuds.")

# --- Tableau recapitulatif ---
print("\n" + "=" * 55)
print("TABLEAU RECAPITULATIF DES EXPERIENCES")
print("=" * 55)
print("1. Modif transaction bloc 2 (sans recalcul) : ECHEC (False)")
print("2. Modif previous_hash bloc 3               : ECHEC (False)")
print("3. Ajout propre d'un 5eme bloc              : REUSSITE (True)")
print("4. Modif bloc 1 (recalcul bloc 1 seulement) : ECHEC (False)")
print("5. Modif bloc 1 (recalcul de toute la chaine): REUSSITE locale (True)")

# --- Partie IV : Questions de comprehension ---
print("\n" + "=" * 55)
print("PARTIE IV : QUESTIONS DE COMPREHENSION")
print("=" * 55)

print("\nQ1 : Qu'est-ce qu'une fonction de hachage cryptographique ?")
print("-> C'est un algorithme mathematique qui transforme n'importe quel texte ou fichier")
print("   en une chaine de caracteres de taille fixe. Elle est a sens unique et")
print("   la moindre modification de l'entree change completement la sortie.")

print("\nQ2 : Quel est le role de SHA-256 dans notre programme ?")
print("-> Il sert a creer une empreinte unique pour chaque bloc a partir de ses donnees.")

print("\nQ3 : Quelle est la difference entre la transaction et le hash d'un bloc ?")
print("-> La transaction est le message stocke (ex: qui envoie quoi a qui).")
print("   Le hash est l'empreinte de securite calculee a partir de ce message et des autres champs.")

print("\nQ4 : Pourquoi chaque bloc doit-il contenir le hash du bloc precedent ?")
print("-> Pour creer la chaine. Si on modifie un bloc ancien, son hash change, ce qui invalide")
print("   tous les blocs d'apres.")

print("\nQ5 : Qu'est-ce que le bloc Genesis ?")
print("-> C'est le tout premier bloc d'une blockchain. Comme il n'a pas de predecesseur,")
print("   son 'previous_hash' vaut '0'.")

print("\nQ6 : Pourquoi avoir cree une classe Bloc en Python ?")
print("-> Pour regrouper proprement dans un meme objet les donnees (index, transaction, hash)")
print("   et le comportement (la methode calculer_hash).")

print("\nQ7 : Pourquoi la blockchain est-elle representee par une liste ?")
print("-> Parce qu'une liste conserve l'ordre chronologique des blocs et permet")
print("   de les parcourir facilement avec un index.")

print("\nQ8 : A quoi sert la fonction verifier_blockchain() ?")
print("-> A controler deux choses : que le contenu de chaque bloc n'a pas bouge,")
print("   et que la liaison entre chaque bloc et son predecesseur est exacte.")

print("\nQ9 : Que se passe-t-il si on change une transaction sans recalculer le hash ?")
print("-> Le hash stocke ne correspond plus au texte du bloc, l'incoherence est")
print("   immediatement detectee.")

print("\nQ10 : Un attaquant peut-il recalculer tous les hashs apres une modification ?")
print("-> Oui sur son propre ordinateur (comme en manipulation 5), mais dans une vraie blockchain")
print("   les autres noeuds ont l'originale et refuseront sa version modifiee.")

print("\nQ11 : Pourquoi ce programme n'est-il pas encore une vraie blockchain ?")
print("-> Parce qu'il tourne en local sur une seule machine. Il n'y a pas de reseau pair-a-pair,")
print("   pas de mecanisme de consensus (PoW/PoS) et pas de signatures de transactions.")

print("\nQ12 : Que faudrait-il ajouter pour en faire une blockchain reelle ?")
print("-> 1. Un reseau de plusieurs noeuds connectes.")
print("   2. Des cles cryptographiques et signatures pour verifier qui envoie les fonds.")
print("   3. Un algorithme de consensus (ex: Proof of Work avec difficulte de calcul).")
