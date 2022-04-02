from . import wrapper

@wrapper.parse
def _encode(b,file_parsed):
	
	uuids = []

	for i in file_parsed:

		uuid = ''

		time_low = i[:4]
		midle = [i[o:o+2] for o in range(4,10,2)]
		midle_len = len(midle)
		node = i[10:]
		
		uuid += time_low.hex() + '-'

		for j in range(midle_len): # midle groups len (time_mid, time_hi_and_version and clock_seq_low)
			uuid += midle[j].hex() + '-'

		uuid += node.hex()

		uuids.append(uuid)

	return uuids
