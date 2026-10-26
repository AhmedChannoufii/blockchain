# TP3 - Exercice 7 : Etude de cas - Tentative de falsification et cout du PoW
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
        self.hash = self.calculer_hash()
        debut = time.perf_counter()
        while not self.hash.startswith(cible):
            self.nonce += 1
            self.hash = self.calculer_hash()
        fin = time.perf_counter()
        return fin - debut

def verifier_blockchain(blockchain, difficulte):
    cible = "0" * difficulte
    for i in range(len(blockchain)):
        bloc = blockchain[i]
        if bloc.hash != bloc.calculer_hash():
            return False, f"Bloc {bloc.index} : contenu falsifie"
        if not bloc.hash.startswith(cible):
            return False, f"Bloc {bloc.index} : preuve de travail invalide"
        if i > 0 and bloc.previous_hash != blockchain[i - 1].hash:
            return False, f"Bloc {bloc.index} : lien brise avec bloc precedent"
    return True, "Chaine valide"

print("=== EXERCICE 7 : Etude du cout d'une modification frauduleuse ===")

difficulte = 3 # On utilise difficulte 3 pour une simulation rapide et representative

print(f"1. Construction et minage de la chaine legitime (4 blocs, difficulte {difficulte})...")
b1 = Bloc(1, "Alice envoie 10 euros a Bob", "0")
b1.miner_bloc(difficulte)

b2 = Bloc(2, "Bob envoie 5 euros a Charlie", b1.hash)
b2.miner_bloc(difficulte)

b3 = Bloc(3, "Charlie envoie 3 euros a David", b2.hash)
b3.miner_bloc(difficulte)

b4 = Bloc(4, "David envoie 1 euro a Alice", b3.hash)
b4.miner_bloc(difficulte)

blockchain = [b1, b2, b3, b4]
valide, msg = verifier_blockchain(blockchain, difficulte)
print("Statut initial :", msg, "(Valide =", valide, ")")

# Falsification du Bloc 2
print("\n2. Attaque : Un pirate modifie la transaction du Bloc 2 (5 -> 500 euros)...")
b2.transaction = "Bob envoie 500 euros a Charlie"

valide_apres_modif, msg_err = verifier_blockchain(blockchain, difficulte)
print(f"Statut immediat : Invalide ! -> {msg_err}")

# Cout de reconstruction : il faut re-miner le bloc 2 ET tous les suivants
print("\n3. Pour masquer la fraude, le pirate doit recalculer et re-miner toute la suite :")
t_debut = time.perf_counter()

# Reminage du bloc 2
b2.miner_bloc(difficulte)
print(f"  - Bloc 2 re-mine : Nonce={b2.nonce}, Hash={b2.hash}")

# Mise a jour et reminage du bloc 3
b3.previous_hash = b2.hash
b3.miner_bloc(difficulte)
print(f"  - Bloc 3 re-mine : Nonce={b3.nonce}, Hash={b3.hash}")

# Mise a jour et reminage du bloc 4
b4.previous_hash = b3.hash
b4.miner_bloc(difficulte)
print(f"  - Bloc 4 re-mine : Nonce={b4.nonce}, Hash={b4.hash}")

t_fin = time.perf_counter()
print(f"\nTemps total depense par l'attaquant pour re-miner les 3 blocs : {t_fin - t_debut:.4f} s")

valide_reconstruite, msg_ok = verifier_blockchain(blockchain, difficulte)
print("Statut local apres re-minage complet :", msg_ok)

# Reponses aux questions de l'etude de cas
print("\n" + "=" * 60)
print("REPONSES AUX QUESTIONS DE L'ETUDE DE CAS")
print("=" * 60)

print("\n--- Travail demande ---")
print("1. Blocs affectes par la modification du Bloc 2 :")
print("   -> Les blocs 2, 3 et 4 sont tous impactes.")

print("\n2. Pourquoi le hash du Bloc 2 doit-il etre recalcule ?")
print("   -> Parce que son contenu textuel a change (500 euros au lieu de 5 euros), ce qui rend")
print("      son ancien hash et son ancien nonce immediatement caducs.")

print("\n3. Pourquoi le Bloc 3 est-il egalement concerne ?")
print("   -> Parce que son champ 'previous_hash' pointait vers l'ancien hash du Bloc 2.")
print("      Des que le Bloc 2 change de hash, le Bloc 3 se retrouve avec un lien brise.")

print("\n4. Operations necessaires pour reconstruire une chaine coherente :")
print("   -> a. Modifier la transaction dans le Bloc 2.")
print("   -> b. Re-miner le Bloc 2 (trouver un nouveau nonce pour valider la difficulte).")
print("   -> c. Mettre a jour previous_hash du Bloc 3 avec le nouveau hash du Bloc 2.")
print("   -> d. Re-miner le Bloc 3 (nouveau nonce).")
print("   -> e. Mettre a jour previous_hash du Bloc 4 et le re-miner a son tour.")

print("\n5. Pourquoi le Proof of Work augmente-t-il le cout de cette operation ?")
print("   -> Parce que chaque bloc a re-miner impose de relancer des milliers de calculs.")
print("      Sans PoW, modifier 3 blocs prend 0.0001 seconde. Avec PoW, chaque bloc coute")
print("      du temps et de l'energie, rendant l'attaque cumulativement plus lourde.")

print("\n--- Questions de reflexion ---")
print("1. Un utilisateur peut-il recalculer les preuves de travail de plusieurs blocs ?")
print("   -> En local sur sa propre machine, oui, il peut faire tourner sa boucle.")

print("\n2. Pourquoi une telle modification devient-elle plus couteuse avec la difficulte ?")
print("   -> Parce que le temps moyen pour re-miner un seul bloc augmente exponentiellement.")
print("      Multiplier ce temps par tous les blocs suivants rend l'effort surhumain.")

print("\n3. Dans une veritable blockchain, pourquoi ne suffit-il pas de modifier sa propre copie ?")
print("   -> Parce que la blockchain vit sur des milliers de noeuds independants (reseau P2P).")
print("      Modifier sa copie locale n'a aucun impact sur les registres des autres participants.")

print("\n4. Quel role jouent les autres participants du reseau ?")
print("   -> Ils verifient chaque proposition de bloc de maniere autonome. Si un noeud tente")
print("      de soumettre une chaine falsifiee, ils la rejettent instantanement.")

print("\n5. Pourquoi la securite depend-elle egalement du mecanisme de consensus ?")
print("   -> Le consensus (comme la regle de la chaine la plus longue / plus grand travail cumule)")
print("      garantit que le reseau s'accorde toujours sur la version honnete majoritaire.")
