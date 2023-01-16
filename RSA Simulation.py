# import rsa

# # Generate a new RSA keypair
# (public_key, private_key) = rsa.newkeys(2048)

# # Get the public key in PEM format
# public_key_pem = rsa.PublicKey.save_pkcs1(public_key, format='PEM')

# # Get the private key in PEM format
# private_key_pem = rsa.PrivateKey.save_pkcs1(private_key, format='PEM')

# # Encrypt some data with the public key
# data = input("Enter the message you want to encrypt: ")
# encrypted_data = rsa.encrypt(data.encode("utf-8"), public_key)

# print("\nOriginal Message:", data)
# print("\nEncrypted Message:", encrypted_data)

# # Decryption
# decrypted_data = rsa.decrypt(encrypted_data, private_key).decode("utf-8")

# print("\nDecrypted Message:", decrypted_data)

import rsa
import time

start_time = time.time()

# Generate a new RSA keypair
(public_key, private_key) = rsa.newkeys(2048)

# Get the public key in PEM format
public_key_pem = rsa.PublicKey.save_pkcs1(public_key, format='PEM')

# Get the private key in PEM format
private_key_pem = rsa.PrivateKey.save_pkcs1(private_key, format='PEM')

# Encrypt some data with the public key
data = input("Enter the message you want to encrypt: ")
encrypted_data = rsa.encrypt(data.encode("utf-8"), public_key)

print("\nPlaintext:", data)
print("\nEncrypted Message/Ciphertext:", encrypted_data)

# Decryption
decrypted_data = rsa.decrypt(encrypted_data, private_key).decode("utf-8")

print("\nDecrypted Message:", decrypted_data)

end_time = time.time()

time_taken = end_time - start_time

print("\nTime taken: ", time_taken, " seconds")
print()
