# Cryptography Basics

**Category:** Cryptography

---

## 🔐 Key Concepts

### Why Cryptography Matters

- Protects confidentiality, integrity, and authenticity of data.
- Required by compliance standards (e.g., PCI DSS for card data).

### Core Terms

- **Plaintext**: Original, unencrypted data.
- **Ciphertext**: Encrypted version of plaintext.
- **Encryption**: Transforming plaintext into ciphertext.
- **Decryption**: Reversing ciphertext back to plaintext.

### Classical Ciphers

- **Caesar Cipher**: Shifts letters by a set amount (e.g., A → D with shift of 3).
  - Easy to break due to only 25 possible shifts.
  - Modern use: educational only.

### Symmetric Encryption

- **Same key** for encryption and decryption.
- **Examples**:
  - **DES**: 56-bit key, deprecated.
  - **AES**: 128, 192, 256-bit key options; standard today.

### XOR Logic

- Useful in stream ciphers:
  - 1 XOR 1 = 0
  - 1 XOR 0 = 1
  - 0 XOR 0 = 0

### Modulo Operation

- Used in key generation and block positions.
  - Example: `118613842 % 9091 = 3565`

---

## 🧪 Useful Commands Summary

### GPG (GNU Privacy Guard)

- Symmetric encryption:
  ```bash
  gpg --symmetric --cipher-algo AES256 message.txt

- Decryption:

    gpg --output message_decrypted.txt --decrypt message.txt.gpg

### OpenSSL

- AES-256-CBC encryption:

openssl aes-256-cbc -e -in message.txt -out encrypted.bin

- AES-256-CBC decryption:

openssl aes-256-cbc -d -in encrypted.bin -out message.txt
