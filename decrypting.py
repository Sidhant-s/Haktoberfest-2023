from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Decrypt a file
def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

# Example usage:
key = generate_key()

file_to_encrypt = "example.txt"
encrypt_file(file_to_encrypt, key)

print("File encrypted. You can now decrypt it.")
input("Press Enter to continue...")

file_to_decrypt = "example.txt"
decrypt_file(file_to_decrypt, key)

print("File decrypted.")
