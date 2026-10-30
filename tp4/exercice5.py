# TP4 - Exercice 5 : Gerer les transactions en attente (Mempool)
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

print("=== EXERCICE 5 : File de transactions en attente ===")

# Test 1 : Liste initiale
soldes1 = {
    "Alice": 100,
    "Bob": 50,
    "Charlie": 30,
    "David": 20
}

transactions_en_attente1 = [
    Transaction("Alice", "Bob", 20),
    Transaction("Bob", "Charlie", 10),
    Transaction("Charlie", "David", 5),
    Transaction("David", "Alice", 100) # David a 25 unites apres reception, insuffisant pour 100
]

valides1 = []
refusees1 = []

for t in transactions_en_attente1:
    if executer_transaction(t, soldes1):
        valides1.append(t)
    else:
        refusees1.append(t)

print("\n--- Execution du lot 1 ---")
print("Transactions valides  :", len(valides1))
for t in valides1:
    print("  [ACCEPTEE]", t)

print("Transactions refusees :", len(refusees1))
for t in refusees1:
    print("  [REFUSEE] ", t)

print("Soldes finaux :", soldes1)

# Test 2 : Modification demandee (David envoie 15 au lieu de 100 + ajout Alice -> Charlie 10)
print("\n--- Execution du lot 2 (montant modifie de David + ajout Alice -> Charlie 10) ---")
soldes2 = {
    "Alice": 100,
    "Bob": 50,
    "Charlie": 30,
    "David": 20
}

transactions_en_attente2 = [
    Transaction("Alice", "Bob", 20),
    Transaction("Bob", "Charlie", 10),
    Transaction("Charlie", "David", 5),
    Transaction("David", "Alice", 15), # modifie : 15 <= 25 (acceptee)
    Transaction("Alice", "Charlie", 10) # nouvelle transaction demandee
]

valides2 = []
refusees2 = []

for t in transactions_en_attente2:
    if executer_transaction(t, soldes2):
        valides2.append(t)
    else:
        refusees2.append(t)

print("Transactions valides  :", len(valides2))
for t in valides2:
    print("  [ACCEPTEE]", t)

print("Transactions refusees :", len(refusees2))
for t in refusees2:
    print("  [REFUSEE] ", t)

print("Soldes finaux :", soldes2)

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Quel est le role de la liste transactions_en_attente ?")
print("-> Elle sert de salle d'attente (mempool) ou les operations demandees par les utilisateurs")
print("   sont stockees temporairement avant d'etre selectionnees, validees et minees.")

print("\nQ2 : Pourquoi utilisons-nous deux listes distinctes pour les transactions acceptees et refusees ?")
print("-> Pour isoler les transactions qui ont reussi (qui iront dans le bloc) de celles qui ont echoue")
print("   (a renvoyer aux utilisateurs ou a annuler).")

print("\nQ3 : Pourquoi l'ordre de traitement des transactions peut-il influencer leur validation ?")
print("-> Parce que chaque transaction met a jour le solde. Un compte peut recevoir des fonds")
print("   dans une transaction A qui lui permettront de financer une transaction B.")
print("   Si B est traitee avant A, elle sera rejetee pour solde insuffisant.")

print("\nQ4 : Une transaction en attente est-elle necessairement valide ?")
print("-> Non. N'importe quel utilisateur peut emettre une requete. C'est le validateur ou mineur")
print("   qui doit verifier sa validite avant de l'inclure dans la chaine.")

print("\nQ5 : Quelle difference existe-t-il entre une transaction acceptee par notre fonction et une transaction confirmee dans une veritable blockchain ?")
print("-> Dans notre script, elle est juste traitee en memoire vive. Dans une vraie blockchain,")
print("   elle doit etre inseree dans un bloc, minee par Proof of Work, validee par l'ensemble du reseau")
print("   et recouverte par plusieurs blocs suivants (confirmations).")
