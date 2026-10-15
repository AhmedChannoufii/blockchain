import hashlib

# ============================================================
# Exercise 4 - Verify blockchain integrity
# TP2: Creating a simple blockchain with Python
# ============================================================

print("=" * 50)
print("EXERCISE 4 - Verify Blockchain Integrity")
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

# --- Build the blockchain ---
bloc1 = Bloc(1, "Alice envoie 10 euros a Bob",      "0")
bloc2 = Bloc(2, "Bob envoie 5 euros a Charlie",      bloc1.hash)
bloc3 = Bloc(3, "Charlie envoie 2 euros a Alice",    bloc2.hash)
blockchain = [bloc1, bloc2, bloc3]

# --- Step 1: Integrity verification function ---
def verifier_blockchain(blockchain):
    for i in range(len(blockchain)):
        bloc = blockchain[i]

        # Verification 1: Is the stored hash still correct?
        if bloc.hash != bloc.calculer_hash():
            print(f"  [FAIL] Block {bloc.index}: hash mismatch (content was modified)")
            return False

        # Verification 2: Does previous_hash point to the right block?
        if i > 0:
            bloc_precedent = blockchain[i - 1]
            if bloc.previous_hash != bloc_precedent.hash:
                print(f"  [FAIL] Block {bloc.index}: broken chain link (previous_hash mismatch)")
                return False

    return True

# --- Step 2: Verify the valid blockchain ---
print("\n[Before modification]")
result = verifier_blockchain(blockchain)
print("Blockchain valide :", result)

# --- Step 3: Tamper with a transaction (without recalculating hash) ---
print("\n[After modifying bloc1.transaction without recalculating hash]")
bloc1.transaction = "Alice envoie 1000 euros a Bob"
result = verifier_blockchain(blockchain)
print("Blockchain valide apres modification :", result)

# --- Questions ---
print("\n--- Answers to Questions ---")
print("Q1. Why must we recalculate the hash to verify a block?")
print("    Because the stored hash might not match the current content.")
print("    Recalculating from scratch tells us if the content was tampered with.")

print("\nQ2. Why is verifying the previous hash necessary?")
print("    It ensures the chain is intact: each block must correctly reference its predecessor.")
print("    A broken link reveals a tampering attempt.")

print("\nQ3. Difference between verifying content vs. verifying the chain link?")
print("    Content check  -> compares stored hash vs recalculated hash of SAME block.")
print("    Chain link check -> compares block[i].previous_hash vs block[i-1].hash.")

print("\nQ4. Is this function enough to secure a real blockchain?")
print("    No! Our program is missing:")
print("    - Decentralized network (multiple nodes)")
print("    - Digital signatures (authentication)")
print("    - Consensus mechanism (Proof of Work / Proof of Stake)")
print("    - Protection against a full chain re-hash attack")
