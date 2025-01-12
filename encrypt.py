import os
import random
import json

def generate_cipher_mapping():
    # English alphabet characters
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shuffled_alphabet = alphabet.copy()
    
    # Shuffle to create a random substitution cipher
    random.shuffle(shuffled_alphabet)
    mapping = dict(zip(alphabet, shuffled_alphabet))
    
    return mapping

def encrypt_plaintext(plaintext, mapping):
    # Encrypt the plaintext using the mapping
    ciphertext = "".join(mapping[char] if char in mapping else char for char in plaintext.upper())
    return ciphertext

def save_mapping_and_ciphertext(mapping, ciphertext):
    # Save the mapping to a file
    with open("cipher_mapping.json", "w") as file:
        json.dump(mapping, file)
    
    # Save the ciphertext to a file
    with open("ciphertext.txt", "w") as file:
        file.write(ciphertext)
    
    print("Cipher mapping and ciphertext saved.")

def main():
    # Load the plaintext
    plaintext_path = "plaintext.txt"
    if not os.path.exists(plaintext_path):
        print(f"Error: {plaintext_path} not found. Run the plaintext generator first.")
        return
    
    with open(plaintext_path, "r") as file:
        plaintext = file.read()
    print(plaintext)
    # Generate the cipher mapping and encrypt the plaintext
    cipher_mapping = generate_cipher_mapping()
    ciphertext = encrypt_plaintext(plaintext, cipher_mapping)
    
    # Save the mapping and ciphertext
    save_mapping_and_ciphertext(cipher_mapping, ciphertext)

if __name__ == "__main__":
    main()
