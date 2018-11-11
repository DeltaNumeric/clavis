# Clavis - Encrypt public repositories
Clavis uses AES for symmetric encryption and decryption as a way to 'lock' publicly accessible data, such as your Git repo.
Clavis will use the provided password to encrypt your data, which will then only be accesible by decrypting with the same password as before.

## Transforming your Git workflow
1. decrypt your repo using your secret key
2. make changes to your code
3. encrypt your repo using the same secret key for decryption
4. push your changes

## Installation
```
pip install clavis
```

## Usage
After running, you will prompted for your password to encrypt the data with
### Encryption
```
$ clavis.py -e
```

### Decryption
```
$ clavis.py -d
```

## .clavrc
Clavis will look for ```.clavrc``` in your current working directory.

Two options are supported:
```
ignore_files = myscript.py, words.txt
ignore_dirs = public
```

## Notes:
* The password field must be of length 16.
  * If it is longer, it will be truncated
  * If it shorter, it will be right-padded by '*'
* Clavis must be run from the **root** of your repo.
* Currently only supported by Python 3
