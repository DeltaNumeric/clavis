# Clavis - Encrypt public repositories
Clavis uses AES for symmetric encryption and decryption as a way to 'lock' publicly accessible data, such as your Git repo.

## Transforming your Git workflow
1. decrypt your repo using your secret key
2. make changes to your code
3. encrypt your repo using the same secret key for decryption
4. push your changes
