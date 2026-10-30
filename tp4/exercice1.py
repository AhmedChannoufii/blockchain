# TP4 - Exercice 1 : Representer une transaction avec Python
# Ahmed Channoufi

class Transaction:
    def __init__(self, expediteur, destinataire, montant):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.montant = montant

    def afficher(self):
        print("Expediteur   :", self.expediteur)
        print("Destinataire :", self.destinataire)
        print("Montant      :", self.montant, "unites")

print("=== EXERCICE 1 : Representation d'une transaction ===")

# Creation des trois transactions demandees
print("\n--- Transaction 1 ---")
transaction1 = Transaction("Alice", "Bob", 20)
transaction1.afficher()

print("\n--- Transaction 2 ---")
transaction2 = Transaction("Bob", "Charlie", 10)
transaction2.afficher()

print("\n--- Transaction 3 ---")
transaction3 = Transaction("Charlie", "David", 5)
transaction3.afficher()

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Quel est le role de la classe Transaction ?")
print("-> Elle sert a modeliser et encapsuler les informations d'un transfert de valeur")
print("   entre deux utilisateurs (qui envoie, qui recoit et combien).")

print("\nQ2 : Pourquoi utilisons-nous une classe plutot qu'une simple chaine de caracteres ?")
print("-> Une classe permet de manipuler les donnees sous forme d'attributs distincts (t.montant,")
print("   t.expediteur), facilitant ainsi les calculs, les controles et les mises a jour de soldes.")

print("\nQ3 : Quelle est l'utilite de la methode afficher() ?")
print("-> Elle permet d'afficher proprement et de maniere lisible le detail de l'operation.")

print("\nQ4 : Quels attributs supplementaires pourrait-on ajouter a une transaction reelle ?")
print("-> Une signature numerique, la cle publique de l'expediteur, un horodatage (timestamp),")
print("   des frais de transaction (fee) et un identifiant unique (hash de la transaction).")
