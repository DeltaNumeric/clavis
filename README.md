# Clavis - Encrypt public repositories
Clavis uses AES for symmetric encryption and decryption as a way to 'lock' publicly accessible data, such as your Git repo.
Clavis will use the provided password to encrypt your data, which will then only be accesible by decrypting with the same password as before.

## Transforming your Git workflow
1. decrypt your repo using your secret key
2. make changes to your code
3. encrypt your repo using the same secret key for decryption
4. push your changes

## Usage

### Encryption
```
$ python clavis.py -e PASSWORD
```

### Decryption
```
$ python clavis.py -d PASSWORD
```

## Notes:
* The password field must be of length 16, 24, or 32.
* Clavis must be run from the **root** of your repo.
