import hashlib

# ============================================================
# Exercise 6 - Experiment with modifications
# TP2: Creating a simple blockchain with Python
# ============================================================

print("=" * 50)
print("EXERCISE 6 - Experiment with Modifications")
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

def build_fresh_blockchain():
    """Returns a fresh, valid 4-block blockchain."""
    b1 = Bloc(1, "Alice envoie 10 euros a Bob",    "0")
    b2 = Bloc(2, "Bob envoie 5 euros a Charlie",    b1.hash)
    b3 = Bloc(3, "Charlie envoie 2 euros a Alice",  b2.hash)
    b4 = Bloc(4, "David envoie 15 euros a Alice",   b3.hash)
    return [b1, b2, b3, b4]

# ===================================================
# Experiment 1: Modify Bloc 2's transaction
#               WITHOUT recalculating its hash
# ===================================================
print("\n--- Experiment 1: Modify Bloc 2 transaction (no hash recalc) ---")
bc = build_fresh_blockchain()
bc[1].transaction = "Bob envoie 9999 euros a Charlie"
# hash NOT recalculated
result1 = verifier_blockchain(bc)
print(f"Verification result: {result1}")
print("Explanation: Bloc 2's stored hash no longer matches its content => FAIL")

# ===================================================
# Experiment 2: Modify Bloc 3's previous_hash
# ===================================================
print("\n--- Experiment 2: Modify Bloc 3's previous_hash ---")
bc = build_fresh_blockchain()
bc[2].previous_hash = "FAKEHASH000"
result2 = verifier_blockchain(bc)
print(f"Verification result: {result2}")
print("Explanation: Bloc 3's previous_hash no longer matches Bloc 2's hash => FAIL")

# ===================================================
# Experiment 3: Correctly add a 5th block
# ===================================================
print("\n--- Experiment 3: Correctly add a 5th block ---")
bc = build_fresh_blockchain()
b5 = Bloc(5, "Eve envoie 7 euros a David", bc[-1].hash)
bc.append(b5)
result3 = verifier_blockchain(bc)
print(f"Verification result: {result3}")
print("Explanation: Bloc 5 correctly references Bloc 4's hash => PASS")

# ===================================================
# Experiment 4: Modify Bloc 1 transaction,
#               recalculate ONLY Bloc 1's hash
# ===================================================
print("\n--- Experiment 4: Modify Bloc 1, recalculate only Bloc 1's hash ---")
bc = build_fresh_blockchain()
bc[0].transaction = "Alice envoie 10000 euros a Bob"
bc[0].hash = bc[0].calculer_hash()  # Bloc 1's hash is now different
# But Bloc 2's previous_hash still points to the OLD hash of Bloc 1
result4 = verifier_blockchain(bc)
print(f"Verification result: {result4}")
print("Explanation: Bloc 1's hash changed, but Bloc 2's previous_hash is stale => FAIL")

# ===================================================
# Experiment 5: Modify Bloc 1, recalculate ALL hashes
# ===================================================
print("\n--- Experiment 5: Modify Bloc 1, recalculate ALL subsequent hashes ---")
bc = build_fresh_blockchain()
# Tamper with Bloc 1
bc[0].transaction = "Alice envoie 10000 euros a Bob"
bc[0].hash = bc[0].calculer_hash()
# Update all subsequent blocks' previous_hash and hash
for i in range(1, len(bc)):
    bc[i].previous_hash = bc[i-1].hash
    bc[i].hash = bc[i].calculer_hash()
result5 = verifier_blockchain(bc)
print(f"Verification result: {result5}")
print("Explanation: All hashes recalculated => local verification PASSES!")
print("BUT in a real blockchain, the network would reject this because:")
print("  - Other nodes have the original chain")
print("  - Proof of Work / Stake makes recalculating all blocks extremely costly")

# ===================================================
# Summary Table
# ===================================================
print("\n" + "=" * 60)
print("RESULTS TABLE")
print("=" * 60)
print(f"{'Experiment':<15} {'Result':<10} {'Explanation'}")
print("-" * 60)
print(f"{'1':<15} {'FAIL' if not result1 else 'PASS':<10} Bloc 2 content changed, hash not updated")
print(f"{'2':<15} {'FAIL' if not result2 else 'PASS':<10} Bloc 3's chain link broken")
print(f"{'3':<15} {'PASS' if result3 else 'FAIL':<10} 5th block added correctly")
print(f"{'4':<15} {'FAIL' if not result4 else 'PASS':<10} Only Bloc 1's hash updated, chain broken at Bloc 2")
print(f"{'5':<15} {'PASS' if result5 else 'FAIL':<10} All hashes updated (bypasses local check, not network)")

# --- Part IV: Comprehension Questions ---
print("\n" + "=" * 60)
print("PART IV - COMPREHENSION QUESTIONS")
print("=" * 60)

answers = {
    "Q1 - What is a cryptographic hash function?":
        "A function that converts data of any size into a fixed-size fingerprint.\n"
        "       It's deterministic, one-way, and collision-resistant.",
    "Q2 - Role of SHA-256 in our program?":
        "Generates a unique 64-character hex fingerprint for each block's content.",
    "Q3 - Difference between transaction and hash?":
        "Transaction: the actual data (e.g., 'Alice sends 10€ to Bob').\n"
        "       Hash: the cryptographic fingerprint calculated FROM that data.",
    "Q4 - Why does each block contain the previous hash?":
        "To link blocks together. Changing any old block breaks all subsequent hashes.",
    "Q5 - What is the Genesis block?":
        "The very first block. It has no predecessor so previous_hash = '0'.",
    "Q6 - Why use a Python class for a block?":
        "Classes bundle data (index, transaction, hash) and behavior (calculer_hash)\n"
        "       into a single reusable structure.",
    "Q7 - Why use a list for the blockchain?":
        "A list maintains order. Blocks are stored sequentially (oldest to newest).",
    "Q8 - Role of verifier_blockchain()?":
        "Checks that no block's content was tampered with AND that all chain links are intact.",
    "Q9 - What happens when a transaction is modified without recalculating hash?":
        "The stored hash no longer matches the content => verifier returns False.",
    "Q10 - Can an attacker recalculate all hashes after modification?":
        "Locally yes (as shown in Experiment 5), but in a real network:\n"
        "       - Proof of Work makes it computationally prohibitive\n"
        "       - Other nodes have the original chain and would reject it",
    "Q11 - Why is our program not a decentralized blockchain?":
        "No network, no peers, no consensus, no cryptographic signatures.",
    "Q12 - What features would make it a real blockchain?":
        "1. P2P network of nodes\n"
        "       2. Digital signatures for authentication\n"
        "       3. Consensus mechanism (PoW or PoS)\n"
        "       4. Distributed storage across multiple nodes",
}

for q, a in answers.items():
    print(f"\n{q}")
    print(f"    {a}")
