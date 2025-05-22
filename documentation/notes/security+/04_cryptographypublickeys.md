# Public Key Cryptography Basics

**Category:** Cryptography

---

## 🔐 Key Concepts

### Asymmetric Encryption

- Uses a **key pair**:
  - **Public Key**: Used to encrypt.
  - **Private Key**: Used to decrypt.

- Main algorithms: **RSA**, **Diffie-Hellman**.

### RSA Explained

- Select primes p and q.
- Calculate n = p × q.
- Compute φ(n) = (p-1)(q-1).
- Choose e (public exponent): 1 < e < φ(n), coprime with φ(n).
- Calculate d (private exponent): `d ≡ e⁻¹ mod φ(n)`.

### Diffie-Hellman (DH)

- Used to generate a shared secret.
- No need to transmit secret directly.

### Digital Certificates & PKI

- Used to validate identity of a public key.
- Common in HTTPS / TLS.

---

## 🧪 Useful Commands Summary

### OpenSSL

- Generate RSA private key:
  ```bash
  openssl genrsa -out private_key.pem 2048

- Extract public key:

   openssl rsa -in private_key.pem -pubout -out public_key.pem

- Encrypt with public key:

   openssl rsautl -encrypt -inkey public_key.pem -pubin -in message.txt -out enc.bin

- Decrypt with private key:

  openssl rsautl -decrypt -inkey private_key.pem -in enc.bin -out message.txt

- View certificate content:

  openssl x509 -in cert.pem -text -noout

- View DH params:

    openssl dhparam -in dhparams.pem -text -noout

### SSH Key Pair Generation

ssh-keygen -t rsa -b 4096
