

import hashlib


def parser():
	with open('inp.txt') as f:
		text = f.read()

	return text.split()[1]


def gethash(start,times = 1):
	count = 0
	output = [None] * 8
	
	default = str(start).encode()
	text = default + str(count).encode()

	while times > 0:

		hashs = hashlib.md5(text).hexdigest()
		if hashs[:5] == '00000' and hashs[5] in "01234567" and output[int(hashs[5])] is None:
			output[int(hashs[5])] = hashs[6]
			print(output,hashs)
			times -= 1


		count += 1
		text = default + str(count).encode()
			

	return "".join(output)



def main(inp):
	print(inp)

	return(gethash(inp,8))



print(main(parser()))

