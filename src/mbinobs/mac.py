from . import wrapper

@wrapper.parse
def _encode(b,file_parsed):

	macs = []
	
	for i in file_parsed:
	
		mac = ''
		mac_list = [i[o].to_bytes(1,'big') for o in range(0,len(i))] # adress groups (1byte), to_bytes --> convert int to bytes
		mac_list_len = len(mac_list)
	
		for j in range(mac_list_len): # groups len 
			mac  += mac_list[j].hex()
			if j < (mac_list_len - 1):
				mac += ":"			
	
		macs.append(mac)

	return macs