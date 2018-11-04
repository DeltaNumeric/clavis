#!/usr/bin/python

import os
import sys
from Crypto.Cipher import AES

def encrypt_file(fname, aes):
	contents = None
	with open(fname, "r") as f:
		contents = f.read()
		contents += (16 - (len(contents) % 16)) * '\n'

	with open(fname, "wb") as f:
		encrypted = aes.encrypt(contents.encode("ISO-8859-1"))
		f.write(encrypted)

def decrypt_file(fname, aes):
	contents = None
	with open(fname, "rb") as f:
		contents = f.read()

	with open(fname, "w") as f:
		decrypted = aes.decrypt(contents).decode("ISO-8859-1")
		f.write(decrypted)

def recursive_encrypt(key, path):
	aes = AES.new(key.encode("utf8"), AES.MODE_CBC)
	for root, dirs, files in os.walk('.'):
		if '.git' in root or '.idea' in root:
			continue

		for f in files:
			if f != "clavis.py":
				encrypt_file(f, aes)

def recursive_decrypt(key, path):
	aes = AES.new(key.encode("utf8"), AES.MODE_CBC)

	for root, dirs, files in os.walk('.'):
		if '.git' in root:
			continue

		for f in files:
			if f != "clavis.py":
				decrypt_file(f, aes)


def main():
	if len(sys.argv) != 3:
		return 1

	key = sys.argv[2]
	l = len(key)

	#if l < 16:
	if l > 16 and l < 24:
		key = key[:15]
	elif l > 24 and l < 32:
		key = key[:23]
	elif l > 32:
		key = key[:31]


	if sys.argv[1] == '-e':
		recursive_encrypt(key, '.')
	elif sys.argv[1] == '-d':
		recursive_decrypt(key, '.')
	else:
		return 1

if __name__ == "__main__":
	sys.exit(main())
