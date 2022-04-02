from . import wrapper

@wrapper.parse
def _encode(b,file_parsed):

	ips = []

	for i in file_parsed:
	
		ip = ''
		ip6_list = [i[o:o+2] for o in range(0,len(i),2)] #  adress group (2bytes)			
		ip6_list_len = len(ip6_list)
		
		for j in range(ip6_list_len):# groups len
			ip += ip6_list[j].hex()
			if j < (ip6_list_len-1):
				ip += ':'

		ips.append(ip)

	return ips