# TP4 - Exercice 8 : Etude de cas - Detection d'une tentative de double depense
# Ahmed Channoufi

class Transaction:
    def __init__(self, expediteur, destinataire, montant):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.montant = montant

    def __str__(self):
        return f"{self.expediteur} -> {self.destinataire} : {self.montant} unites"

def valider_transaction(transaction, soldes):
    if transaction.expediteur not in soldes:
        return False, "Expediteur inexistant"
    if transaction.destinataire not in soldes:
        return False, "Destinataire inexistant"
    if type(transaction.montant) not in (int, float):
        return False, "Montant invalide"
    if transaction.montant <= 0:
        return False, "Montant <= 0"
    if soldes[transaction.expediteur] < transaction.montant:
        return False, f"Solde insuffisant (solde={soldes[transaction.expediteur]}, demande={transaction.montant})"
    return True, "Valide"

def executer_transaction(transaction, soldes):
    valide, msg = valider_transaction(transaction, soldes)
    if valide:
        soldes[transaction.expediteur] -= transaction.montant
        soldes[transaction.destinataire] += transaction.montant
        return True, msg
    return False, msg

print("=== EXERCICE 8 : Etude de cas - Double depense ===")

# --- EXPERIENCE 1 : Ordre 40 unites puis 30 unites ---
print("\n" + "=" * 55)
print("EXPERIENCE 1 : Traitement 40 unites (vers Bob) puis 30 unites (vers Charlie)")
print("=" * 55)
soldes_exp1 = {"Alice": 50, "Bob": 20, "Charlie": 10}
print("Soldes initiaux :", soldes_exp1)

t1_a = Transaction("Alice", "Bob", 40)
t2_a = Transaction("Alice", "Charlie", 30)

res1_a, msg1_a = executer_transaction(t1_a, soldes_exp1)
print(f"1. Traitement T1 ({t1_a}) : {'ACCEPTEE' if res1_a else 'REFUSEE'} -> {msg1_a}")
print("   Soldes intermediaires :", soldes_exp1)

res2_a, msg2_a = executer_transaction(t2_a, soldes_exp1)
print(f"2. Traitement T2 ({t2_a}) : {'ACCEPTEE' if res2_a else 'REFUSEE'} -> {msg2_a}")
print("   Soldes finaux         :", soldes_exp1)
solde_final_alice_1 = soldes_exp1["Alice"]

# --- EXPERIENCE 2 : Ordre inverse (30 unites puis 40 unites) ---
print("\n" + "=" * 55)
print("EXPERIENCE 2 : Traitement inverse 30 unites (vers Charlie) puis 40 unites (vers Bob)")
print("=" * 55)
soldes_exp2 = {"Alice": 50, "Bob": 20, "Charlie": 10}
print("Soldes initiaux :", soldes_exp2)

t1_b = Transaction("Alice", "Charlie", 30)
t2_b = Transaction("Alice", "Bob", 40)

res1_b, msg1_b = executer_transaction(t1_b, soldes_exp2)
print(f"1. Traitement T1 ({t1_b}) : {'ACCEPTEE' if res1_b else 'REFUSEE'} -> {msg1_b}")
print("   Soldes intermediaires :", soldes_exp2)

res2_b, msg2_b = executer_transaction(t2_b, soldes_exp2)
print(f"2. Traitement T2 ({t2_b}) : {'ACCEPTEE' if res2_b else 'REFUSEE'} -> {msg2_b}")
print("   Soldes finaux         :", soldes_exp2)
solde_final_alice_2 = soldes_exp2["Alice"]

# Tableau a completer
print("\n" + "=" * 65)
print("TABLEAU RECAPITULATIF DE LA DOUBLE DEPENSE")
print("=" * 65)
print(f"{'Ordre de traitement':<26} | {'Transaction 1':<13} | {'Transaction 2':<13} | {'Solde final Alice':<15}")
print("-" * 65)
print(f"{'40 unites puis 30 unites':<26} | {'Acceptee':<13} | {'Refusee':<13} | {solde_final_alice_1:<15}")
print(f"{'30 unites puis 40 unites':<26} | {'Acceptee':<13} | {'Refusee':<13} | {solde_final_alice_2:<15}")
print("=" * 65)

# Reponses aux questions
print("\n=== Reponses aux questions ===")
print("Q1 : Pourquoi les deux transactions ne peuvent-elles pas etre acceptees ensemble ?")
print("-> Parce que la somme des deux transferts (40 + 30 = 70 unites) depasse le solde total")
print("   d'Alice (50 unites). Une fois la premiere executee, il ne reste plus assez pour la deuxieme.")

print("\nQ2 : Pourquoi l'ordre de traitement est-il important ?")
print("-> L'ordre determine quel destinataire recevra reellement les fonds et qui sera refuse.")
print("   Dans le cas 1, Bob est paye et Charlie est rejete. Dans le cas 2, c'est l'inverse.")

print("\nQ3 : Comment notre fonction empeche-t-elle cette double depense simplifiee ?")
print("-> En mettant a jour le solde d'Alice en temps reel apres la premiere transaction,")
print("   la deuxieme transaction echoue au controle : if soldes[expediteur] < montant.")

print("\nQ4 : Pourquoi ce probleme est-il particulierement important dans une monnaie numerique ?")
print("-> Parce qu'un fichier numerique se duplique facilement sans cout. Sans controle strict,")
print("   un utilisateur pourrait copier sa monnaie et payer plusieurs commercants avec les memes pieces.")

print("\nQ5 : Dans une veritable blockchain, pourquoi faut-il egalement verifier l'autorisation et parvenir a un accord sur l'ordre ?")
print("-> 1. L'autorisation (signature electronique) prouve que le detenteur legitime a ordonne le paiement.")
print("   2. L'accord sur l'ordre (consensus) est vital car dans un reseau distribue, les noeuds peuvent")
print("      recevoir les deux transactions dans un ordre different. Le consensus fige un ordre unique.")
