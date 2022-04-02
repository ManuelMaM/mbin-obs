#!/usr/bin/env python3
"""Obfuscate binary data into ipv4/ipv6/uuid/mac addresses and returns formated list :0"""

def main(method,bfile):

	m = {

	'ipv4' : ipv4._encode,
	'ipv6' : ipv6._encode,
	'uuid' : uuid._encode,
	'mac' : mac._encode

	}
	
	try:
		encoded = m[method](bfile)	

	except KeyError:

		print('Please use one of the methods : ipv4/ipv6/mac/uuid')
		exit(0)

	print(f"Binary encoded as {method}:")
	print(encoded)

if __name__ == "__main__":

	from mbinobs import ipv4,ipv6,mac,uuid

	from sys import exit,argv

	try:

		path = argv[1]
		method = argv[2]
		bfile = open(path,'rb').read()

	except IndexError:

		print('Please pass binary file and method as argument: python main.py "/path/to/bin" ipv4 ')
		exit(0)

	except FileNotFoundError:

		print(f'Could not find file {path}')
		exit(0)
	
	main(method,bfile)

else:
	from IPfuscation import *