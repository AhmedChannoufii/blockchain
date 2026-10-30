# TP5 - Exercice 7 : Combiner signature et verification du solde
# Ahmed Channoufi

import json
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey
)
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

class Portefeuille:
    def __init__(self):
        self.cle_privee = Ed25519PrivateKey.generate()
        self.cle_publique = self.cle_privee.public_key()

    def obtenir_adresse(self):
        cle_bytes = self.cle_publique.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        return cle_bytes.hex()

    def signer(self, message):
        return self.cle_privee.sign(message.encode("utf-8"))

class Transaction:
    def __init__(self, expediteur, destinataire, montant):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.montant = montant
        self.signature = None

    def obtenir_message(self):
        donnees = {
            "expediteur": self.expediteur,
            "destinataire": self.destinataire,
            "montant": self.montant
        }
        return json.dumps(
            donnees,
            sort_keys=True,
            separators=(",", ":")
        )

    def signer(self, portefeuille):
        if portefeuille.obtenir_adresse() != self.expediteur:
            raise ValueError("Portefeuille non autorise")
        self.signature = portefeuille.signer(self.obtenir_message())

    def verifier_signature(self):
        if self.signature is None:
            return False

        try:
            cle_bytes = bytes.fromhex(self.expediteur)
            cle_publique = Ed25519PublicKey.from_public_bytes(cle_bytes)
            cle_publique.verify(
                self.signature,
                self.obtenir_message().encode("utf-8")
            )
            return True
        except (InvalidSignature, ValueError):
            return False

def valider_transaction(transaction, soldes):
    # 1. Verification de la signature cryptographique (authenticite et integrite)
    if not transaction.verifier_signature():
        return False, "Signature invalide ou absente"

    # 2. Existence de l'expediteur
    if transaction.expediteur not in soldes:
        return False, "Expediteur inconnu"

    # 3. Existence du destinataire
    if transaction.destinataire not in soldes:
        return False, "Destinataire inconnu"

    # 4. Validite du type du montant
    if type(transaction.montant) is not int:
        return False, "Le montant doit etre un entier"

    # 5. Positivite stricte
    if transaction.montant <= 0:
        return False, "Montant inferieur ou egal a zero"

    # 6. Solde suffisant
    if soldes[transaction.expediteur] < transaction.montant:
        return False, "Solde insuffisant"

    return True, "Valide"

def executer_transaction(transaction, soldes):
    valide, msg = valider_transaction(transaction, soldes)
    if not valide:
        return False, msg

    soldes[transaction.expediteur] -= transaction.montant
    soldes[transaction.destinataire] += transaction.montant
    return True, msg

def afficher_soldes_lisibles(soldes, noms):
    print("  Etat des soldes :")
    for addr, solde in soldes.items():
        nom = noms.get(addr, addr[:8] + "...")
        print(f"    {nom:<8} ({addr[:12]}...) : {solde} unites")

print("=== EXERCICE 7 : Validation complete (Signature + Soldes) ===")

# Creation des portefeuilles
alice = Portefeuille()
bob = Portefeuille()
charlie = Portefeuille()

noms = {
    alice.obtenir_adresse(): "Alice",
    bob.obtenir_adresse(): "Bob",
    charlie.obtenir_adresse(): "Charlie"
}

# Initialisation des soldes avec les adresses publiques
soldes = {
    alice.obtenir_adresse(): 100,
    bob.obtenir_adresse(): 50,
    charlie.obtenir_adresse(): 30
}

afficher_soldes_lisibles(soldes, noms)

# Test 1 : Transaction 1 (Alice -> Bob, 20 unites) signee et executee
print("\n--- Test 1 : Alice envoie 20 unites a Bob (signee par Alice) ---")
t1 = Transaction(alice.obtenir_adresse(), bob.obtenir_adresse(), 20)
t1.signer(alice)
ok1, msg1 = executer_transaction(t1, soldes)
print("Execution T1 :", ok1, f"({msg1})")
afficher_soldes_lisibles(soldes, noms)

# Test 2 : Transaction 2 (Bob -> Charlie, 15 unites) signee et executee
print("\n--- Test 2 : Bob envoie 15 unites a Charlie (signee par Bob) ---")
t2 = Transaction(bob.obtenir_adresse(), charlie.obtenir_adresse(), 15)
t2.signer(bob)
ok2, msg2 = executer_transaction(t2, soldes)
print("Execution T2 :", ok2, f"({msg2})")
afficher_soldes_lisibles(soldes, noms)

# Test 3 : Transaction dont le montant depasse le solde (Bob tente 200 unites)
print("\n--- Test 3 : Bob tente d'envoyer 200 unites a Alice (solde insuffisant) ---")
t3 = Transaction(bob.obtenir_adresse(), alice.obtenir_adresse(), 200)
t3.signer(bob)
ok3, msg3 = executer_transaction(t3, soldes)
print("Execution T3 :", ok3, f"({msg3})")

# Test 4 : Transaction modifiee apres signature (20 -> 50)
print("\n--- Test 4 : Modification frauduleuse apres signature (Alice -> Bob 20 modifiee a 50) ---")
t4 = Transaction(alice.obtenir_adresse(), bob.obtenir_adresse(), 20)
t4.signer(alice)
t4.montant = 50 # modification en douce
ok4, msg4 = executer_transaction(t4, soldes)
print("Execution T4 :", ok4, f"({msg4})")

# Test 5 : Transaction sans signature
print("\n--- Test 5 : Tentative d'executer une transaction sans signature ---")
t5 = Transaction(alice.obtenir_adresse(), bob.obtenir_adresse(), 10)
ok5, msg5 = executer_transaction(t5, soldes)
print("Execution T5 :", ok5, f"({msg5})")

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Pourquoi devons-nous verifier la signature et le solde ?")
print("-> La signature prouve l'authenticite et le consentement de l'expediteur.")
print("   Le solde prouve que l'expediteur a les moyens financiers de payer.")

print("\nQ2 : Quelle verification permet de detecter une modification de la transaction ?")
print("-> transaction.verifier_signature() : elle recalcule la verification Ed25519 sur le contenu.")

print("\nQ3 : Quelle verification permet de detecter un montant superieur au solde ?")
print("-> La comparaison : if soldes[transaction.expediteur] < transaction.montant:")

print("\nQ4 : Pourquoi la validation doit-elle preceder la modification des soldes ?")
print("-> Pour eviter d'appliquer un transfert frauduleux, invalide ou insolvable sur les comptes.")

print("\nQ5 : Quels autres controles faudrait-il ajouter pour construire un systeme de paiement plus realiste ?")
print("-> Des nonces de transaction (ou horodatages) pour empecher les attaques par rejeu (replay attack),")
print("   la deduction de frais de reseau (fees), et un mecanisme de consensus distribue.")
