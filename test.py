import binascii, itertools, base64, sys
def xor_crypt_string(data, key='estoesunaclaveparacifrar', encode=False, decode=False):
	from itertools import izip, cycle
	import base64
	if decode:
		data = base64.decodestring(data)
	xored = ('').join(chr(ord(x) ^ ord(y)) for x, y in izip(data, cycle(key)))
	if encode:
		return base64.encodestring(xored).strip()
	return xored	
secret_data = 'Ax8VCB4HEAAGDDMEBRERPhENAh8DLQQcEQERMAgaBjERAhwEGgADHA=='
claro = xor_crypt_string(secret_data,decode=True)
print (claro)
