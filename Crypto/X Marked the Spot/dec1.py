from itertools import cycle

# Known part of the plaintext
known_plaintext = b"uiuctf{"
# Length of the known part of the plaintext
pt_length = len(known_plaintext)

# Read the ciphertext from file
with open("ct", "rb") as ct_file:
    ct = ct_file.read()

# Brute-force the last byte of the key
for i in range(256):
    # Construct the key by XORing the known part of the plaintext and ciphertext
    partial_key = bytes(ct[j] ^ known_plaintext[j] for j in range(pt_length))
    full_key = partial_key + bytes([i])
    
    # Decrypt the ciphertext using the generated key
    plaintext = bytes(x ^ y for x, y in zip(ct, cycle(full_key)))
    
    # Check if the plaintext starts with the known pattern
    if plaintext.startswith(known_plaintext):
        print(f"Possible key: {full_key}")
        print(f"Possible plaintext: {plaintext.decode('utf-8', errors='replace')}")
        print("-" * 50)
