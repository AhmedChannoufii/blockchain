# TP3 - Exercice 2 : Modifier la difficulte du minage
# Ahmed Channoufi

import hashlib
import time

def miner_avec_difficulte(message, difficulte):
    nonce = 0
    cible = "0" * difficulte
    debut = time.perf_counter()
    
    while True:
        contenu = message + str(nonce)
        hash_resultat = hashlib.sha256(contenu.encode("utf-8")).hexdigest()
        if hash_resultat.startswith(cible):
            break
        nonce += 1
        
    fin = time.perf_counter()
    duree = fin - debut
    tentatives = nonce + 1
    return difficulte, nonce, hash_resultat, tentatives, duree

print("=== EXERCICE 2 : Mesure de l'impact de la difficulte ===")

message = "Blockchain"
difficultes = [1, 2, 3, 4]
resultats = []

print(f"\nMinage du message '{message}' pour differentes difficultes :")

for d in difficultes:
    diff, n, h, tent, duree = miner_avec_difficulte(message, d)
    resultats.append((diff, tent, duree, h, n))
    print(f"\n[Difficulte {diff}]")
    print(f"  Nonce trouve    : {n}")
    print(f"  Tentatives      : {tent}")
    print(f"  Temps de minage : {duree:.6f} secondes")
    print(f"  Hash obtenu     : {h}")

# Tableau recapitulatif
print("\n" + "=" * 65)
print("TABLEAU DES MESURES (EXERCICE 2)")
print("=" * 65)
print(f"{'Difficulte':<12} | {'Nombre de tentatives':<22} | {'Temps (secondes)':<18}")
print("-" * 65)
for diff, tent, duree, _, _ in resultats:
    print(f"{diff:<12} | {tent:<22} | {duree:<18.6f}")
print("=" * 65)

# Reponses aux questions du TP
print("\n=== Reponses aux questions ===")
print("Q1 : Comment evolue le nombre de tentatives lorsque la difficulte augmente ?")
print("-> Le nombre de tentatives augmente de maniere exponentielle. En moyenne, chaque zero")
print("   hexadecimal supplementaire multiplie le nombre d'essais theoriques par 16 (16, 256, 4096, 65536...).")

print("\nQ2 : Comment evolue le temps de minage ?")
print("-> Le temps de minage suit directement l'augmentation des tentatives : il passe de fractions")
print("   de millisecondes a plusieurs centiemes ou dixiemes de seconde, et explose aux difficultes plus elevees.")

print("\nQ3 : Le temps de minage augmente-t-il toujours de maniere reguliere ?")
print("-> Pas toujours de maniere lineaire ou exactement proportionnelle a chaque essai individuel,")
print("   car le hachage est probabiliste : on peut avoir la 'chance' de trouver le hash valide")
print("   au debut de la recherche ou au contraire devoir tester beaucoup plus de nonces.")

print("\nQ4 : Pourquoi deux difficultes successives peuvent-elles produire des temps tres differents ?")
print("-> Parce que l'espace des solutions est reduit d'un facteur 16 a chaque increment de difficulte.")
print("   La marche entre deux difficultes est un palier exponentiel, pas une simple addition.")

print("\nQ5 : Quel est l'interet d'augmenter la difficulte dans un systeme Proof of Work ?")
print("-> Dans un reseau reel, elle permet d'ajuster le temps entre deux blocs malgre la montee")
print("   de la puissance de calcul des mineurs (ex: environ 10 minutes par bloc sur Bitcoin).")
print("   Elle empeche qu'un attaquant ne produise des blocs instantanement.")
