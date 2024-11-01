

import math

def parser():
	with open('inp.txt') as f:
		text = f.read()

	return [tuple(map(int,i.split())) for i in text.split("\n")]



def istriangle(lengths):
	return sum(lengths[:2]) > lengths[2]

def main(inp):
	count = 0

	for i in inp:
		if istriangle(sorted(i)):
			count += 1

	return count



print(main(parser()))

