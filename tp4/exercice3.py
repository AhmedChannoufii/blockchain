# TP4 - Exercice 3 : Valider une transaction
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
    # 1. Verification de l'existence de l'expediteur
    if transaction.expediteur not in soldes:
        return False, "Expediteur inconnu"

    # 2. Verification de l'existence du destinataire
    if transaction.destinataire not in soldes:
        return False, "Destinataire inconnu"

    # 3. Verification du type du montant
    if type(transaction.montant) not in (int, float):
        return False, "Montant invalide (non numerique)"

    # 4. Verification de la positivite stricte du montant
    if transaction.montant <= 0:
        return False, "Montant inferieur ou egal a zero"

    # 5. Verification de la disponibilite des fonds
    if soldes[transaction.expediteur] < transaction.montant:
        return False, "Solde insuffisant"

    return True, "Transaction valide"

print("=== EXERCICE 3 : Validation d'une transaction ===")

# Tests du sujet
t1 = Transaction("Alice", "Bob", 30)
t2 = Transaction("Charlie", "David", 100)

val1, msg1 = valider_transaction(t1, soldes)
val2, msg2 = valider_transaction(t2, soldes)

print("\n--- Tests de base ---")
print(f"Transaction 1 (Alice -> Bob, 30)   : {val1} ({msg1})")
print(f"Transaction 2 (Charlie -> David, 100): {val2} ({msg2})")

# Tests des cas limites demandes dans le travail
print("\n--- Tests des cas limites demandes ---")

cas_tests = [
    ("Montant egal a zero", Transaction("Alice", "Bob", 0)),
    ("Montant negatif", Transaction("Alice", "Bob", -10)),
    ("Expediteur inconnu", Transaction("Inconnu", "Bob", 10)),
    ("Destinataire inconnu", Transaction("Alice", "Inconnu", 10)),
    ("Montant > solde", Transaction("Alice", "Bob", 150))
]

for label, t in cas_tests:
    v, msg = valider_transaction(t, soldes)
    print(f"{label:<22} : {str(v):<5} ({msg})")

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Pourquoi doit-on verifier l'existence de l'expediteur ?")
print("-> Pour savoir a quel compte debiter les fonds. Si le compte n'existe pas,")
print("   on ne peut pas verifier son solde.")

print("\nQ2 : Pourquoi doit-on verifier que le montant est positif ?")
print("-> Pour empecher un montant nul (inutile) ou negatif (ce qui reviendrait a voler")
print("   de l'argent au destinataire au lieu de lui en envoyer).")

print("\nQ3 : Quelle condition permet de detecter un solde insuffisant ?")
print("-> La comparaison : if soldes[transaction.expediteur] < transaction.montant:")

print("\nQ4 : Que signifie la valeur False retournee par la fonction ?")
print("-> La transaction viole au moins une des regles de gestion et doit etre rejetee.")

print("\nQ5 : Cette fonction permet-elle de verifier que la transaction a reellement ete autorisee par l'expediteur ?")
print("-> Non. Elle verifie uniquement les regles de solde et de format. Dans une vraie blockchain,")
print("   c'est la signature cryptographique (cle privee) qui prouve le consentement de l'expediteur.")
