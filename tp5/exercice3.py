# TP5 - Exercice 3 : Verifier une signature numerique
# Ahmed Channoufi

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.exceptions import InvalidSignature

print("=== EXERCICE 3 : Verification d'une signature numerique ===")

# Generation des cles
cle_privee = Ed25519PrivateKey.generate()
cle_publique = cle_privee.public_key()

# Message original et signature
message = "Alice envoie 20 unites a Bob"
message_bytes = message.encode("utf-8")
signature = cle_privee.sign(message_bytes)

# Test 1 : Verification normale avec le message original
print("\n--- Test 1 : Verification du message original ---")
print("Message signe :", message)
try:
    cle_publique.verify(signature, message_bytes)
    print("Resultat      : Signature valide (l'expediteur possede bien la cle privee et le message est intact)")
except InvalidSignature:
    print("Resultat      : Signature invalide")

# Test 2 : Modification du montant (20 -> 200 unites)
print("\n--- Test 2 : Tentative de modification du montant (20 -> 200) ---")
message_altere = "Alice envoie 200 unites a Bob"
print("Message teste :", message_altere)
try:
    cle_publique.verify(signature, message_altere.encode("utf-8"))
    print("Resultat      : Signature valide")
except InvalidSignature:
    print("Resultat      : Signature invalide (modification detectee !)")

# Test 3 : Modification du destinataire (Bob -> Charlie)
print("\n--- Test 3 : Tentative de modification du destinataire (Bob -> Charlie) ---")
message_altere_dest = "Alice envoie 20 unites a Charlie"
print("Message teste :", message_altere_dest)
try:
    cle_publique.verify(signature, message_altere_dest.encode("utf-8"))
    print("Resultat      : Signature valide")
except InvalidSignature:
    print("Resultat      : Signature invalide (usurpation/modification detectee !)")

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Quelle cle permet de verifier une signature ?")
print("-> La cle publique (cle_publique).")

print("\nQ2 : Quel est le role de la methode verify() ?")
print("-> Elle prend la signature et le message en octets, et verifie mathematiquement")
print("   si la signature a bien ete calculee sur ce message avec la cle privee associee.")
print("   Si ce n'est pas le cas, elle leve l'exception InvalidSignature.")

print("\nQ3 : Pourquoi la verification peut-elle echouer ?")
print("-> Soit parce que le message a ete altere apres sa signature,")
print("   soit parce que la signature provient d'une autre cle privee.")

print("\nQ4 : Une signature reste-t-elle valide si le message est modifie ?")
print("-> Non, jamais. La moindre difference dans les octets fait echouer la verification.")

print("\nQ5 : Comment ce mecanisme contribue-t-il a l'integrite des transactions ?")
print("-> Il garantit qu'aucun intermediaire ou pirate ne peut modifier le montant, l'expediteur")
print("   ou le destinataire d'une transaction en transit sans invalider instantanement sa signature.")
