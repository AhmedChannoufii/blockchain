# TP4 - Exercice 2 : Gerer les soldes des utilisateurs
# Ahmed Channoufi

print("=== EXERCICE 2 : Gestion des soldes ===")

soldes = {
    "Alice": 100,
    "Bob": 50,
    "Charlie": 30,
    "David": 20
}

def afficher_soldes(soldes):
    for utilisateur, solde in soldes.items():
        print(f"  {utilisateur:<8} : {solde} unites")
    print("  Total en circulation :", sum(soldes.values()), "unites")

print("\n--- Soldes initiaux ---")
afficher_soldes(soldes)

# 1. Transfert de 20 unites d'Alice vers Bob
print("\n--- Apres transfert 1 : Alice -> Bob (20 unites) ---")
soldes["Alice"] -= 20
soldes["Bob"] += 20
afficher_soldes(soldes)

# 2. Transfert de 10 unites de Bob vers Charlie
print("\n--- Apres transfert 2 : Bob -> Charlie (10 unites) ---")
soldes["Bob"] -= 10
soldes["Charlie"] += 10
afficher_soldes(soldes)

# 3. Transfert de 5 unites de Charlie vers David
print("\n--- Apres transfert 3 : Charlie -> David (5 unites) ---")
soldes["Charlie"] -= 5
soldes["David"] += 5
afficher_soldes(soldes)

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Comment le solde de l'expediteur est-il modifie ?")
print("-> Il est diminue du montant envoye : soldes[expediteur] -= montant.")

print("\nQ2 : Comment le solde du destinataire est-il modifie ?")
print("-> Il est augmente du meme montant : soldes[destinataire] += montant.")

print("\nQ3 : Quelle est la somme totale des soldes avant les transferts ?")
print("-> 100 + 50 + 30 + 20 = 200 unites.")

print("\nQ4 : Quelle est la somme totale des soldes apres les transferts ?")
print("-> 80 + 60 + 35 + 25 = 200 unites. La somme reste constante (loi de conservation).")

print("\nQ5 : Que se passerait-il si Alice essayait d'envoyer 200 unites sans verification ?")
print("-> Son solde deviendrait negatif (80 - 200 = -120 unites), ce qui creerait de la valeur")
print("   a partir de rien et fausserait la coherence financiere du registre.")
