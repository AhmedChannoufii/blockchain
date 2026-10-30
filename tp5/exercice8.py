import json
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey
)
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature


class Portefeuille:
    def __init__(self):
        self._cle_privee = Ed25519PrivateKey.generate()
        self.cle_publique = self._cle_privee.public_key()

    def obtenir_adresse(self):
        octets = self.cle_publique.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        return octets.hex()

    def signer(self, message):
        return self._cle_privee.sign(
            message.encode("utf-8")
        )


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
    if not transaction.verifier_signature():
        return False
    if transaction.expediteur not in soldes:
        return False
    if transaction.destinataire not in soldes:
        return False
    if transaction.montant <= 0:
        return False
    if soldes[transaction.expediteur] < transaction.montant:
        return False
    return True


def executer_transaction(transaction, soldes):
    if not valider_transaction(transaction, soldes):
        return False
    soldes[transaction.expediteur] -= transaction.montant
    soldes[transaction.destinataire] += transaction.montant
    return True


def afficher_soldes(soldes, adresses):
    for nom, adr in adresses.items():
        print(f"    {nom:<8} ({adr[:12]}...) : {soldes[adr]} unites")


if __name__ == "__main__":
    print("=== EXERCICE 8 : Etude de cas - Tentative d'usurpation d'identite ===\n")

    # 1. Creation des 3 portefeuilles
    alice = Portefeuille()
    bob = Portefeuille()
    charlie = Portefeuille()

    adresses = {
        "Alice": alice.obtenir_adresse(),
        "Bob": bob.obtenir_adresse(),
        "Charlie": charlie.obtenir_adresse()
    }

    # 2. Initialisation des soldes
    soldes = {
        alice.obtenir_adresse(): 100,
        bob.obtenir_adresse(): 50,
        charlie.obtenir_adresse(): 30
    }

    print("Soldes initiaux :")
    afficher_soldes(soldes, adresses)
    print()

    # 3. Bob tente de transferer 80 unites d'Alice vers lui-meme
    print("--- SITUATION 1 : Tentative d'usurpation par Bob (Alice -> Bob, 80 unites) ---")
    tx_frauduleuse = Transaction(
        alice.obtenir_adresse(),
        bob.obtenir_adresse(),
        80
    )

    # 4 & 5. Tentative de signature avec le portefeuille de Bob
    print("Bob tente de signer la transaction avec son propre portefeuille...")
    try:
        tx_frauduleuse.signer(bob)
        print("Signature reussie (inattendu !)")
    except ValueError as e:
        print(f"ECHEC detecte par la methode signer() : {e}")

    # Que se passerait-il si Bob contourne signer() en forcant sa propre signature ?
    print("\nBob tente de contourner le controle en signant directement avec sa cle privee :")
    tx_frauduleuse.signature = bob.signer(tx_frauduleuse.obtenir_message())
    print("Signature forcee de Bob injectee dans la transaction.")
    
    valide = tx_frauduleuse.verifier_signature()
    print(f"Verification cryptographique avec l'adresse d'Alice : {valide}")
    
    succes = executer_transaction(tx_frauduleuse, soldes)
    print(f"Tentative d'execution sur le reseau : {succes} (Transaction refusee)")
    print("Soldes apres tentative frauduleuse (aucun changement) :")
    afficher_soldes(soldes, adresses)
    print()

    # 6. Transaction legitime realisee et signee par Alice
    print("--- SITUATION 2 : Transaction legitime signee par Alice (Alice -> Bob, 20 unites) ---")
    tx_legitime = Transaction(
        alice.obtenir_adresse(),
        bob.obtenir_adresse(),
        20
    )
    tx_legitime.signer(alice)
    print(f"Verification cryptographique de la signature d'Alice : {tx_legitime.verifier_signature()}")
    
    succes_legitime = executer_transaction(tx_legitime, soldes)
    print(f"Execution sur le reseau : {succes_legitime} (Transaction acceptee)")
    print("Soldes apres transaction legitime :")
    afficher_soldes(soldes, adresses)

    # Questions
    print("\n=== Reponses aux questions ===")
    print("Q1 : Pourquoi Bob ne devrait-il pas pouvoir signer une transaction a la place d'Alice ?")
    print("-> Parce que cela lui permettrait de voler les fonds d'Alice sans son consentement, violant l'integrite du systeme.")
    print("Q2 : Quel est le role de la cle privee dans cette protection ?")
    print("-> La cle privee est le secret absolu detenant le pouvoir de depense. Seule Alice possede sa cle privee Ed25519.")
    print("Q3 : Pourquoi la cle publique ne permet-elle pas de produire une signature valide ?")
    print("-> Le probleme mathematique sous-jacent (courbes elliptiques) est a sens unique : on ne peut pas forger de signature avec la seule cle publique.")
    print("Q4 : Que se passerait-il si Bob obtenait la cle privee d'Alice ?")
    print("-> Bob pourrait signer n'importe quelle transaction au nom d'Alice, et le reseau la considererait comme valide.")
    print("Q5 : Pourquoi la protection des cles privees est-elle essentielle dans une blockchain ?")
    print("-> Dans une blockchain decentralisee, il n'existe pas d'autorite centrale pour annuler un vol. La cle privee EST la propriete des fonds.")
