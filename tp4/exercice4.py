# TP4 - Exercice 4 : Executer une transaction valide
# Ahmed Channoufi

class Transaction:
    def __init__(self, expediteur, destinataire, montant):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.montant = montant

soldes = {
    "Alice": 100,
    "Bob": 50,
    "Charlie": 30,
    "David": 20
}

def valider_transaction(transaction, soldes):
    if transaction.expediteur not in soldes:
        return False
    if transaction.destinataire not in soldes:
        return False
    if type(transaction.montant) not in (int, float):
        return False
    if transaction.montant <= 0:
        return False
    if soldes[transaction.expediteur] < transaction.montant:
        return False
    return True

def executer_transaction(transaction, soldes):
    if valider_transaction(transaction, soldes):
        soldes[transaction.expediteur] -= transaction.montant
        soldes[transaction.destinataire] += transaction.montant
        return True
    return False

def afficher_etat(label, soldes):
    print(f"\n--- {label} ---")
    for u, s in soldes.items():
        print(f"  {u:<8} : {s} unites")
    print("  Somme totale :", sum(soldes.values()), "unites")

print("=== EXERCICE 4 : Execution securisee des transactions ===")
afficher_etat("Soldes initiaux", soldes)

# 1. Transaction 1 : Alice -> Bob (30 unites)
t1 = Transaction("Alice", "Bob", 30)
res1 = executer_transaction(t1, soldes)
print(f"\nExecution T1 (Alice -> Bob, 30) : {res1}")
afficher_etat("Soldes apres T1", soldes)

# 2. Transaction 2 : Bob -> Charlie (20 unites)
t2 = Transaction("Bob", "Charlie", 20)
res2 = executer_transaction(t2, soldes)
print(f"\nExecution T2 (Bob -> Charlie, 20) : {res2}")
afficher_etat("Soldes apres T2", soldes)

# 3. Transaction 3 : Charlie -> David (15 unites)
t3 = Transaction("Charlie", "David", 15)
res3 = executer_transaction(t3, soldes)
print(f"\nExecution T3 (Charlie -> David, 15) : {res3}")
afficher_etat("Soldes apres T3", soldes)

# 4. Transaction 4 : David -> Alice (200 unites - refus attendu)
t4 = Transaction("David", "Alice", 200)
res4 = executer_transaction(t4, soldes)
print(f"\nExecution T4 (David -> Alice, 200) : {res4} (Refusee car David a seulement {soldes['David']} unites)")
afficher_etat("Soldes apres T4 (inchanges)", soldes)

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Pourquoi la fonction appelle-t-elle valider_transaction() ?")
print("-> Pour s'assurer que toutes les conditions sont remplies avant de modifier les soldes.")

print("\nQ2 : A quel moment les soldes sont-ils modifies ?")
print("-> Uniquement APRES la validation positive (si valider_transaction renvoie True).")

print("\nQ3 : Que se passe-t-il lorsqu'une transaction est refusee ?")
print("-> La fonction retourne False et aucun solde n'est modifie (le registre reste intact).")

print("\nQ4 : Pourquoi est-il important de valider une transaction avant de l'executer ?")
print("-> Pour eviter d'inscrire des operations incoherentes ou d'avoir des soldes negatifs.")

print("\nQ5 : Quel probleme pourrait apparaitre si plusieurs transactions etaient executees sans tenir compte des soldes mis a jour ?")
print("-> Le risque de double depense : un utilisateur pourrait depenser son solde plusieurs fois")
print("   en envoyant simultanement plusieurs transferts.")
