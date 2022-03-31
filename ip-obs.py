#!/usr/bin/env python3
"""Encode binary data into ipv4 or ipv6 adress and returns formated list :0"""

import sys

def ip_encode(bfile,v):
	
	file_parsed = [bfile[i:i+v] for i in range(0,len(bfile),v)] # separete initial bytes string into 4/16 bytes (ipv4/6  adress lengh)
	ips=[]
	
	for i in file_parsed:
	
		ip = ''
		if (v == 4):

			ip_list = [i[o] for o in range(0,len(i))] # adress groups (1byte)

			if (len(bfile) % v): #padd ip with 0 if necessary
				while (len(ip_list) < v):
					ip_list.append(0)

			for j in range(4):
				a = str(ip_list[j])
				ip  += f'{a}'
				if j < 3:
					ip += "."			
		
		elif (v == 16):
			
			ip6_list = [i[o:o+2] for o in range(0,len(i),2)] # separete adress group (2bytes)			
		
			if (len(bfile) % v): #padd ip with 0 if necessary
				
				while len(ip6_list[-1]) < 2:
					ip6_list[-1] += b'\x00'
				while (len(ip6_list) < v):
					ip6_list.append(b'\x00\x00')

			for j in range(8):
				ip += ip6_list[j].hex()
				if j < 7:
					ip += ':'
		
		ips.append(ip)

	return ips

def main():
	v = {
	'ipv4': 4,
	'ipv6': 16
	}

	try:

		path = sys.argv[1]
		method = sys.argv[2]
		bfile = open(path,'rb').read()
		print(ip_encode(bfile,v[method]))	

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
