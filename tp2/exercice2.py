import hashlib

# ============================================================
# Exercise 2 - Create your first block
# TP2: Creating a simple blockchain with Python
# ============================================================

print("=" * 50)
print("EXERCISE 2 - Create Your First Block")
print("=" * 50)

# --- Step 2: Define the Bloc class ---
class Bloc:
    def __init__(self, index, transaction, previous_hash):
        self.index = index
        self.transaction = transaction
        self.previous_hash = previous_hash
        # Hash is automatically calculated when the block is created
        self.hash = self.calculer_hash()

    def calculer_hash(self):
        """Calculate the SHA-256 hash of the block's content."""
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

# --- Step 3: Create a Bloc object ---
bloc1 = Bloc(
    1,
    "Alice envoie 10 euros a Bob",
    "0"
)

print("\n--- Block 1 ---")
print("Index        :", bloc1.index)
print("Transaction  :", bloc1.transaction)
print("Hash precedent:", bloc1.previous_hash)
print("Hash actuel  :", bloc1.hash)

# --- Modification: 10 euros -> 100 euros ---
print("\n--- After modifying: 10 euros -> 100 euros ---")
bloc1_modified = Bloc(
    1,
    "Alice envoie 100 euros a Bob",   # <-- modified
    "0"
)
print("Index        :", bloc1_modified.index)
print("Transaction  :", bloc1_modified.transaction)
print("Hash precedent:", bloc1_modified.previous_hash)
print("Hash actuel  :", bloc1_modified.hash)

print("\n--- Comparison ---")
print("Original hash :", bloc1.hash)
print("Modified hash :", bloc1_modified.hash)
print("Same hash?    :", bloc1.hash == bloc1_modified.hash)

# --- Questions ---
print("\n--- Answers to Questions ---")
print("Q1. Role of __init__():")
print("    It's the constructor: called automatically when creating a new Bloc object.")
print("    It initializes index, transaction, previous_hash, and calculates the hash.")

print("\nQ2. Role of self.hash = self.calculer_hash():")
print("    Automatically computes and stores the block's hash at creation time.")

print("\nQ3. Why is index converted to string?")
print("    sha256() needs bytes, so we build a string first.")
print("    str(self.index) converts integer (e.g. 1) to '1' for string concatenation.")

print("\nQ4. Which attributes are used to calculate the hash?")
print("    index + transaction + previous_hash (joined with '|')")

print("\nQ5. What happens after modifying the transaction?")
print("    The hash completely changes — even a small change produces a very different hash.")
