# TP3 - Exercice 6 : Etudier l'influence de la difficulte et trace graphique
# Ahmed Channoufi

import hashlib
import time
import os
import matplotlib.pyplot as plt

class Bloc:
    def __init__(self, index, transaction, previous_hash):
        self.index = index
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculer_hash()

    def calculer_hash(self):
        contenu = (
            str(self.index)
            + "|"
            + self.transaction
            + "|"
            + self.previous_hash
            + "|"
            + str(self.nonce)
        )
        return hashlib.sha256(contenu.encode("utf-8")).hexdigest()

    def miner_bloc(self, difficulte):
        cible = "0" * difficulte
        while not self.hash.startswith(cible):
            self.nonce += 1
            self.hash = self.calculer_hash()

print("=== EXERCICE 6 : Mesures et courbe de difficulte ===")

difficultes = [1, 2, 3, 4]
temps_mesures = []
tentatives_mesurees = []

print("\nLancement des mesures de minage...")
for difficulte in difficultes:
    bloc = Bloc(1, "Alice envoie 10 euros a Bob", "0")
    debut = time.perf_counter()
    bloc.miner_bloc(difficulte)
    fin = time.perf_counter()
    
    duree = fin - debut
    nb_tentatives = bloc.nonce + 1
    
    temps_mesures.append(duree)
    tentatives_mesurees.append(nb_tentatives)
    
    print(f"Difficulte : {difficulte}")
    print(f"  Nonce trouve : {bloc.nonce}")
    print(f"  Tentatives   : {nb_tentatives}")
    print(f"  Temps        : {duree:.6f} secondes")
    print(f"  Hash         : {bloc.hash}")
    print("-" * 40)

# Tableau recapitulatif des resultats
print("\n" + "=" * 60)
print("TABLEAU DES MESURES (EXERCICE 6)")
print("=" * 60)
print(f"{'Difficulte':<12} | {'Nombre de tentatives':<22} | {'Temps (secondes)':<18}")
print("-" * 60)
for d, tent, t in zip(difficultes, tentatives_mesurees, temps_mesures):
    print(f"{d:<12} | {tent:<22} | {t:<18.6f}")
print("=" * 60)

# Generation et sauvegarde du graphique Matplotlib
dossier_actuel = os.path.dirname(os.path.abspath(__file__))
chemin_image = os.path.join(dossier_actuel, "graphique_difficulte.png")

plt.figure(figsize=(8, 5))
plt.plot(difficultes, temps_mesures, marker="o", color="#2563eb", linewidth=2, markersize=8)
plt.xlabel("Difficulte (nombre de zeros)", fontsize=11)
plt.ylabel("Temps de minage (secondes)", fontsize=11)
plt.title("Influence de la difficulte sur le temps de minage (Proof of Work)", fontsize=12, fontweight="bold")
plt.xticks(difficultes)
plt.grid(True, linestyle="--", alpha=0.6)

# Annotations sur les points
for d, t in zip(difficultes, temps_mesures):
    plt.annotate(f"{t:.4f}s", (d, t), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9)

plt.tight_layout()
plt.savefig(chemin_image, dpi=150)
print(f"\n[OK] Graphique sauvegarde avec succes dans : {chemin_image}")

# Reponses aux questions
print("\n=== Reponses aux questions ===")
print("Q1 : Quelle relation observez-vous entre la difficulte et le temps de minage ?")
print("-> La relation est exponentielle : chaque pallier de difficulte demande sensiblement")
print("   plus de calculs et fait grimper le temps de resolution.")

print("\nQ2 : Pourquoi le temps de minage augmente-t-il generalement avec la difficulte ?")
print("-> Parce que chaque zero impose en base 16 reduit la proportion de hashs valides d'un")
print("   facteur 16 (probabilite 1/16, puis 1/256, 1/4096, 1/65536...). Le nombre de nonces")
print("   a essayer avant de trouver la bonne empreinte explose statistiquement.")

print("\nQ3 : Le nombre de tentatives est-il proportionnel a la difficulte ?")
print("-> Non, il n'est pas proportionnel (lineaire), il est exponentiel (puissance de 16).")
print("   Passer de 1 a 4 zeros ne multiplie pas le travail par 4, mais par environ 4 096.")

print("\nQ4 : Pourquoi les resultats peuvent-ils varier d'un ordinateur a un autre ?")
print("-> Pour deux raisons :")
print("   1. La puissance brute du processeur (frequence, nombre de hashs calculables par seconde).")
print("   2. La charge systeme au moment de l'execution.")

print("\nQ5 : Quel serait l'effet d'une difficulte tres elevee sur les performances du systeme ?")
print("-> Les blocs prendraient des heures ou des jours a etre mines, le reseau deviendrait extremement")
print("   lent a valider les transactions et la consommation electrique augmenterait drastiquement.")
