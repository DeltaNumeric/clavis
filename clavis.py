#!/usr/bin/python

import os
import sys
import pyaes

def encrypt_file(fname, aes):
	contents = None
	with open(fname, "r") as f:
		contents = f.read()
		contents += (16 - (len(contents) % 16)) * '\n'
		contents = contents.encode("utf-8")

	with open(fname, "wb") as f:
		encrypted = aes.encrypt(contents)
		f.write(encrypted)

def decrypt_file(fname, aes):
	contents = None
	with open(fname, "rb") as f:
		contents = f.read()

	with open(fname, "w") as f:
		decrypted = aes.decrypt(contents)
		decrypted = remove_trailing_nl(decrypted.decode("utf-8"))
		f.write(decrypted)

def recursive_encrypt(key, path):
	key = key.encode("utf-8")
	aes = pyaes.AESModeOfOperationCTR(key)
	for root, dirs, files in os.walk('.'):
		if '.git' in root or '.idea' in root:
			continue

		for f in files:
			if f != "clavis.py" and f != "README.md":
				encrypt_file(f, aes)

def recursive_decrypt(key, path):
	key = key.encode("utf-8")
	aes = pyaes.AESModeOfOperationCTR(key)

	for root, dirs, files in os.walk('.'):
		if '.git' in root or '.idea' in root:
			continue

		for f in files:
			if f != "clavis.py" and f != "README.md":
				decrypt_file(f, aes)

def remove_trailing_nl(string):
	while len(string) > 1:
		hit = False
		if string[-2] == '\n':
			string = string[:len(string)-1]
			hit = True
		if not hit:
			break

	return string


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
		return recursive_encrypt(key, '.')
	elif sys.argv[1] == '-d':
		return recursive_decrypt(key, '.')
	else:
		return 1

if __name__ == "__main__":
	sys.exit(main())
