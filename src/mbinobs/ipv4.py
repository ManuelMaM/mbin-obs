from . import wrapper

@wrapper.parse
def _encode(b,file_parsed):

	ips = []

	for i in file_parsed:
	
		ip = ''
		ip_list = [i[o] for o in range(0,len(i))] # adress groups (1byte)
		ip_list_len = len(ip_list)

		for j in range(ip_list_len): # groups len 
			ip  += str(ip_list[j])
			if j < (ip_list_len - 1):
				ip += "."			
	
		ips.append(ip)

	return ips