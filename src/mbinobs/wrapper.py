import sys

def parse(func):

	method = list(sys._current_frames().values())[0].f_back.f_globals['__name__'] #https://stackoverflow.com/questions/1095543/get-name-of-calling-functions-module-in-python#1095621
	method_bytes = {
		'mbinobs.ipv4' : 4,
		'mbinobs.ipv6' : 16,
		'mbinobs.uuid' :	16,
		'mbinobs.mac' : 6
	}
	
	def wrapper_parse(bfile: bytes) -> bytes:
		
		try:
			if type(bfile) != bytes:
				raise AssertionError
		except AssertionError:
			print((f"{method} accepts <class 'bytes'>, not {type(bfile)}"))
			sys.exit(0)
			
		b = method_bytes[method]
		bfile_len = len(bfile)
		file_parsed = [bfile[i:i+b] for i in range(0,bfile_len,b)] # initial byte string sapareted into method lenght(bytes)
		
		if (bfile_len % b): #padd ip with 0 if necessary
			while (len(file_parsed[-1]) < b):
				file_parsed[-1] += b'\x00'

		return func(b,file_parsed)

	return wrapper_parse	