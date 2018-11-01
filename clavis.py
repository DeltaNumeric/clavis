import os
import sys

def recursive_encrypt(key):
	print('-e ', key)

def recursive_decrypt(key):
	print('-d ', key)

def main():
	if len(sys.argv) != 3:
		return 1

	if sys.argv[1] == '-e':
		recursive_encrypt(sys.argv[2])
	elif sys.argv[1] == '-d':
		recursive_decrypt(sys.argv[2])
	else:
		return 1
	
	return 0 

if __name__ == "__main__":
	sys.exit(main())
