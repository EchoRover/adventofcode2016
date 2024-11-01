

import math

def parser():
	with open('inp.txt') as f:
		text = f.read()

	return [tuple(map(int,i.split())) for i in text.split("\n")]

def transpose(grid):
	xlen = len(grid[0])
	ylen = len(grid)
	newgrid = [[None] * ylen for i in range(xlen)]
	for i in range(ylen):
		for j in range(xlen):
			newgrid[j][i] = grid[i][j]

	newgrid = [i[j:j + 3] for i in newgrid for j in range(0,len(i),3) ]
	return newgrid



def istriangle(lengths):
	return sum(lengths[:2]) > lengths[2]

def main(inp):
	count = 0

	for i in inp:
		if istriangle(sorted(i)):
			count += 1

	return count

# print(transpose([[1,2],[3,4],[5,6]]))

print(main(transpose(parser())))

