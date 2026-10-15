import hashlib

# ============================================================
# Exercise 3 - Build a blockchain of three blocks
# TP2: Creating a simple blockchain with Python
# ============================================================

print("=" * 50)
print("EXERCISE 3 - Build a Blockchain of 3 Blocks")
print("=" * 50)

# --- Bloc class (reused from Exercise 2) ---
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

# --- Step 2: Create the blocks ---
# Genesis block (Bloc 1) — previous_hash = "0" (no predecessor)
bloc1 = Bloc(
    1,
    "Alice envoie 10 euros a Bob",
    "0"
)

# Bloc 2 references Bloc 1's hash
bloc2 = Bloc(
    2,
    "Bob envoie 5 euros a Charlie",
    bloc1.hash
)

# Bloc 3 references Bloc 2's hash
bloc3 = Bloc(
    3,
    "Charlie envoie 2 euros a Alice",
    bloc2.hash
)

# --- Step 3: Create the blockchain ---
blockchain = [bloc1, bloc2, bloc3]

# --- Step 4: Display the blocks ---
print("\n--- Blockchain ---")
for bloc in blockchain:
    print("----------------------")
    print("Bloc         :", bloc.index)
    print("Transaction  :", bloc.transaction)
    print("Hash precedent:", bloc.previous_hash)
    print("Hash actuel  :", bloc.hash)

# --- Verify chaining visually ---
print("\n--- Chain verification ---")
print(f"Bloc 1 hash      : {bloc1.hash}")
print(f"Bloc 2 prev_hash : {bloc2.previous_hash}")
print(f"Match?           : {bloc1.hash == bloc2.previous_hash}")
print()
print(f"Bloc 2 hash      : {bloc2.hash}")
print(f"Bloc 3 prev_hash : {bloc3.previous_hash}")
print(f"Match?           : {bloc2.hash == bloc3.previous_hash}")

# --- Questions ---
print("\n--- Answers to Questions ---")
print("Q1. How are blocks linked together?")
print("    Each block stores the hash of the previous block in 'previous_hash'.")

print("\nQ2. Why does Bloc 2 use bloc1.hash?")
print("    To create a cryptographic link — Bloc 2 'knows' Bloc 1's fingerprint.")

print("\nQ3. Why does Bloc 3 use bloc2.hash?")
print("    Same principle — every block in the chain references the one before it.")

print("\nQ4. What is the role of the blockchain list?")
print("    It stores all blocks in order, forming the chain from oldest to newest.")

print("\nQ5. What happens if we replace bloc1.hash with '12345' when creating Bloc 2?")
bloc2_fake = Bloc(2, "Bob envoie 5 euros a Charlie", "12345")
print(f"    Bloc 2 would have previous_hash='12345' but Bloc 1's real hash is:")
print(f"    {bloc1.hash}")
print("    => The chain would be broken/inconsistent!")
