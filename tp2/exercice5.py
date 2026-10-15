import hashlib

# ============================================================
# Exercise 5 - Add a fourth block
# TP2: Creating a simple blockchain with Python
# ============================================================

print("=" * 50)
print("EXERCISE 5 - Add a Fourth Block")
print("=" * 50)

# --- Bloc class ---
class Bloc:
    def __init__(self, index, transaction, previous_hash):
        self.index = index
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.hash = self.calculer_hash()

    def calculer_hash(self):
        contenu = (
            str(self.index)
            + "|"
            + self.transaction
            + "|"
            + self.previous_hash
        )
        return hashlib.sha256(
            contenu.encode("utf-8")
        ).hexdigest()

# --- Integrity verifier ---
def verifier_blockchain(blockchain):
    for i in range(len(blockchain)):
        bloc = blockchain[i]
        if bloc.hash != bloc.calculer_hash():
            return False
        if i > 0:
            if bloc.previous_hash != blockchain[i - 1].hash:
                return False
    return True

# --- Build the 3-block blockchain from Exercise 3 ---
bloc1 = Bloc(1, "Alice envoie 10 euros a Bob",    "0")
bloc2 = Bloc(2, "Bob envoie 5 euros a Charlie",    bloc1.hash)
bloc3 = Bloc(3, "Charlie envoie 2 euros a Alice",  bloc2.hash)

# --- Add the 4th block ---
bloc4 = Bloc(
    4,
    "David envoie 15 euros a Alice",
    bloc3.hash   # previous hash = Bloc 3's hash
)

# --- Create the 4-block blockchain ---
blockchain = [bloc1, bloc2, bloc3, bloc4]

# --- Display all 4 blocks ---
print("\n--- Full Blockchain (4 blocks) ---")
for bloc in blockchain:
    print("----------------------")
    print("Bloc         :", bloc.index)
    print("Transaction  :", bloc.transaction)
    print("Hash precedent:", bloc.previous_hash)
    print("Hash actuel  :", bloc.hash)

# --- Verify integrity ---
print("\n--- Integrity Check ---")
print("Blockchain valide :", verifier_blockchain(blockchain))

# --- Questions ---
print("\n--- Answers to Questions ---")
print("Q1. Which hash should be used as Bloc 4's previous hash?")
print(f"    bloc3.hash = {bloc3.hash}")

print("\nQ2. Why not use Bloc 1's hash?")
print("    Blockchain is sequential. Bloc 4 must reference its direct predecessor (Bloc 3).")
print("    Using Bloc 1's hash would break the chain and fail verification.")

print("\nQ3. What happens if Bloc 4 has an incorrect previous hash?")
# Simulate wrong previous hash
bloc4_wrong = Bloc(4, "David envoie 15 euros a Alice", "WRONGHASH123")
blockchain_wrong = [bloc1, bloc2, bloc3, bloc4_wrong]
print("    Verification result with wrong hash:", verifier_blockchain(blockchain_wrong))
print("    => Returns False — the chain link from Bloc 3 to Bloc 4 is broken.")
