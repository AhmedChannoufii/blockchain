import hashlib

# ============================================================
# Exercise 1 - Discover SHA-256
# TP2: Creating a simple blockchain with Python
# ============================================================

print("=" * 50)
print("EXERCISE 1 - Discover SHA-256")
print("=" * 50)

# --- Step 2: Calculate a hash ---
texte = "Blockchain"
hash_texte = hashlib.sha256(
    texte.encode("utf-8")
).hexdigest()

print("\nTexte :", texte)
print("Hash  :", hash_texte)

# --- Step 3: Experiment ---
print("\n--- Experiments ---")

# 1. lowercase 'blockchain'
texte2 = "blockchain"
hash2 = hashlib.sha256(texte2.encode("utf-8")).hexdigest()
print(f"\nTexte : {texte2}")
print(f"Hash  : {hash2}")

# 2. longer text
texte3 = "Blockchain et cryptographie"
hash3 = hashlib.sha256(texte3.encode("utf-8")).hexdigest()
print(f"\nTexte : {texte3}")
print(f"Hash  : {hash3}")

# --- Questions ---
print("\n--- Answers to Questions ---")
print("Q1. Do different inputs produce the same hash?")
print("    No! 'Blockchain' and 'blockchain' produce completely different hashes.")
print(f"    'Blockchain'              -> {hash_texte}")
print(f"    'blockchain'              -> {hash2}")
print(f"    'Blockchain et crypto...' -> {hash3}")

print(f"\nQ2. What is the length of a SHA-256 hash in hexadecimal characters?")
print(f"    Length: {len(hash_texte)} characters (256 bits = 32 bytes = 64 hex characters)")

print("\nQ3. Does the length of the text influence the length of the hash?")
print(f"    No! All three hashes are {len(hash_texte)} chars regardless of input length.")

print("\nQ4. Why is hashing useful in a blockchain?")
print("    - Each block gets a unique 'fingerprint'.")
print("    - Any modification to a block changes its hash.")
print("    - This makes tampering detectable.")

print("\nQ5. Can we easily find the original text from the hash?")
print("    No! SHA-256 is a one-way function (preimage resistance).")
print("    It's computationally infeasible to reverse a hash.")
