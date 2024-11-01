

import hashlib


def parser():
	with open('inp.txt') as f:
		text = f.read()

	return text.split()[1]


def gethash(start,times = 1):
	count = 0
	output = ""
	default = str.encode(start)
	text = default + str(count).encode()

	while times > 0:

		hashs = hashlib.md5(text).hexdigest()
		if hashs[:5] == '00000':
			output += hashs[5]
			times -= 1


		count += 1
		text = default + str(count).encode()
		
	return output



def main(inp):
	print(inp)

	return(gethash(inp,8))



print(main(parser()))

