"""
Generate RSA Public and Private Keys

This script generates RSA public and private keys using the cryptography library.

Author: Indrajit Ghosh
Created On: Sep 27, 2023

Requirements:
- Install the cryptography library: pip install cryptography

Usage:
- Run this script to generate RSA keys.
- The generated keys will be saved in separate PEM files: rsa_private_key.pem and rsa_public_key.pem.

"""

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_rsa_keys():
    """
    Generate RSA public and private keys.

    Returns:
        private_key (bytes): The private key in PEM format.
        public_key (bytes): The public key in PEM format.
    """
    # Generate an RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,  # Commonly used value for the public exponent
        key_size=2048,  # You can adjust the key size as needed
        backend=default_backend()
    )

    # Serialize the private key to PEM format
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Get the corresponding public key
    public_key = private_key.public_key()

    # Serialize the public key to PEM format
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_key_pem, public_key_pem

if __name__ == "__main__":
    # Generate RSA keys
    private_key_pem, public_key_pem = generate_rsa_keys()

    # Save the keys to files
    with open("rsa_private_key.pem", "wb") as private_key_file:
        private_key_file.write(private_key_pem)
    with open("rsa_public_key.pem", "wb") as public_key_file:
        public_key_file.write(public_key_pem)

    print("RSA keys generated and saved as rsa_private_key.pem and rsa_public_key.pem.")
