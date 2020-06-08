#!/usr/bin/python3

import pyfiglet
from hashlib import *
import sys
from base64 import *

banner = pyfiglet.figlet_format("HASH_CRACKER")
banner1 = pyfiglet.figlet_format("By s1m00.3x3", font="digital")
print(banner)
print(banner1)

def hashing():

	options = int((input("[+] Choose The hash Type you wanna Crack \n[1]=> md5 \n[2]=> sha1 \n[3]=> sha256 \n[4]=> base64 \n[0]=> quit \n[+] What Can i Do For You => ")))

	if options == 1:

		md5 = input("Enter Your Hash ===> ");
		
		wlist = input("Enter Your Wordlist Path ==> ")

		file = open(wlist,"r+").readlines()

		for passwds in file:

			count = 0

			h = md5(passwds.strip().encode()).hexdigest()
		
			print("Trying Passwords ==>",count,passwds.strip())
			count += 1
			
			if h == md5:

				print("**********************************")
				print("[+] Password Found [+] ==> ",passwds)
				print("**********************************")
				hashing()

	if options == 2:

		sha1 = input("Enter Your Hash ===> ");
		
		wlist = input("Enter Your Wordlist Path ==> ")

		file = open(wlist,"r+").readlines()

		for passwds in file:

			count = 0

			h = sha1(passwds.strip().encode()).hexdigest()
		
			print("Trying Passwords ==>",count,passwds.strip())
			count += 1
			
			if h == sha1:

				print("**********************************")
				print("[+] Password Found [+] ==> ",passwds)
				print("**********************************")
				hashing()		

	if options == 3:

		sha256 = input("Enter Your Hash ===> ");
		
		wlist = input("Enter Your Wordlist Path ==> ")

		file = open(wlist,"r+").readlines()

		for passwds in file:

			count = 0

			h = sha256(passwds.strip().encode()).hexdigest()
			
			print("Trying Passwords ==>",count,passwds.strip())
			count += 1
			
			if h == sha256:
				print("**********************************")
				print("[+] Password Found [+] ==> ",passwds)
				print("**********************************")
				hashing()

	if options == 4:

		b64 = input("Enter Your Base64 ===> ");
		b64 = b64.encode("UTF-8")
		decoded = b64decode(b64)
		print("**********************************")
		print("Done ===> ",decoded);
		print("**********************************")
		hashing()


	if options == 0:
		sys.exit()					

hashing()
