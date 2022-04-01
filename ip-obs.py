#!/usr/bin/env python3
"""Obfuscate binary data into ipv4 or ipv6 addresses and returns formated list :0"""

import sys

def ipv4_encode(bfile):

	b = 4
	file_parsed = [bfile[i:i+b] for i in range(0,len(bfile),b)] # initial byte string into 4 bytes (ipv4 adress lengh)
	ips = []
	
	for i in file_parsed:
	
		ip = ''
		ip_list = [i[o] for o in range(0,len(i))] # adress groups (1byte)

		if (len(bfile) % b): #padd ip up with 0 if necessary
			while (len(ip_list) < b):
				ip_list.append(0)

		for j in range(4):

			a = str(ip_list[j])
			ip  += f'{a}'
			if j < 3:
				ip += "."			
	
		ips.append(ip)

	return ips

def ipv6_encode(bfile):

	b = 16 #bytes
	file_parsed = [bfile[i:i+b] for i in range(0,len(bfile),b)] # initial byte string into 16 bytes (ipv6  adress lengh)
	ips = []

	for i in file_parsed:
	
		ip = ''
		ip6_list = [i[o:o+2] for o in range(0,len(i),2)] #  adress group (2bytes)			
		
		if (len(bfile) % b): #padd ip with 0 if necessary
			
			while len(ip6_list[-1]) < 2:
				ip6_list[-1] += b'\x00'
			while (len(ip6_list) < b):
				ip6_list.append(b'\x00\x00')

			for j in range(8):
				ip += ip6_list[j].hex()
				if j < 7:
					ip += ':'

		ips.append(ip)

	return ips
		
def main():
	v = {
	'ipv4': ipv4_encode,
	'ipv6': ipv6_encode
	}

	try:

		path = sys.argv[1]
		method = sys.argv[2]
		bfile = open(path,'rb').read()
		print(v[method](bfile))	

	except IndexError:

		print('Please pass binary file and method as argument: python main.py "/path/to/bin" ipv4 ')
		sys.exit(1)

	except FileNotFoundError:

		print(f'Could not find file {path}')
		sys.exit(1)

	except KeyError:
		print('Please use method : ipv4/ipv6')



if __name__ == "__main__":
	main()
