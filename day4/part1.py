

import math

def parser():
	with open('inp.txt') as f:
		text = f.read()

	return text.split("\n")

def getunique(text):
	uni = {}
	for i in text:
		if i not in uni:
			uni[i] = 1
		else:
			uni[i] += 1
	fin = [(i,uni[i]) for i in uni]

	return sorted(sorted(fin,key = lambda a:a[0]),key = lambda a: a[1],reverse = True)

def isroom(room):
	checksum = room[room.rfind("[") + 1:len(room) - 1]
	name = room[:room.rfind('-')]
	sectorid = room[room.rfind('-') + 1:room.find("[")]
	name = "".join(name.split("-"))

	uni = getunique(name)

	if all([checksum[i] == uni[i][0] for i in range(5)]):
		return int(sectorid)
	return 0




def main(inp):

	count = 0
	
	for i in inp:
		count += isroom(i)
	return count



print(main(parser()))

