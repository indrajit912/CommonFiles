"""
Generate RSA Public and Private Keys using the rsa module

This script generates RSA public and private keys using the rsa module.

Author: Indrajit Ghosh
Created On: Sep 13, 2022

Requirements:
- Install the rsa module: pip install rsa

Usage:
- Run this script to generate RSA keys.
- The generated keys will be saved in separate PEM files: rsa_private_key.pem and rsa_public_key.pem.

"""

import rsa

def generate_rsa_keys():
    """
    Generate RSA public and private keys.

    Returns:
        private_key (str): The private key in PEM format.
        public_key (str): The public key in PEM format.
    """
    # Generate an RSA key pair with a specified key size (e.g., 2048 bits)
    key = rsa.newkeys(2048)

    # Convert the private key to PEM format
    private_key = key[1].save_pkcs1().decode()

    # Convert the public key to PEM format
    public_key = key[0].save_pkcs1().decode()

    return private_key, public_key

if __name__ == "__main__":
    # Generate RSA keys
    private_key_pem, public_key_pem = generate_rsa_keys()

    # Save the keys to files
    with open("rsa_private_key.pem", "w") as private_key_file:
        private_key_file.write(private_key_pem)
    with open("rsa_public_key.pem", "w") as public_key_file:
        public_key_file.write(public_key_pem)

    print("RSA keys generated and saved as rsa_private_key.pem and rsa_public_key.pem.")
