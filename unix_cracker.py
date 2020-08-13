import os
import sys
import hashlib
from crypt import crypt

def test(pas):
	d = open(sys.argv[1], 'r')
	for l in d.readlines():
		word = l.strip('\n')
		salt = pas[0:2]
		c = crypt(word, salt)
		if c == pas:
			print("[+] Found Password: " + word)
			return
	print("[-] No password found")
	return
 


def main():
	if len(sys.argv) == 3:
		dic = sys.argv[1]
		file = sys.argv[2]
		if not os.path.isfile(dic):
			print("[-] Error: " + dic + " no such file")
			exit(0)
		if not os.path.isfile(file):
			print("[-] Error: " + file + "no such file")
			exit(0)
		if not os.access(file, os.R_OK):
			print("[-] Permission Denied for " + file)
			exit(0)
		if not os.access(dic, os.R_OK):
			print("[-] Permission Denied for " + dic)
			exit(0)
		f = open(file, "r")
		for line in f.readlines():
			if ":" in line:
				line.strip('\n')
				user = line.split(':')[0]
				print("[*] Cracking password for: " + user)
				pas = line.split(':')[1].strip()
				if not pas == "*" and not pas == 'x' and not pas == '!':
					test(pas)
				else:
					print("[+] User " + user + " has no password")
			else:
				print("[-] Error: Wrong File")
	else:
		print("[-] Usage: python3 unix_cracker.py dictionary.txt password.txt")
		exit(0)


if __name__ == "__main__":
	main()
