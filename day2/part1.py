

import math

def parser():
	with open('inp.txt') as f:
		text = f.read()

	return text.split("\n")


GRID = [[1,2,3],[4,5,6],[7,8,9]]

def getkey(startcoords,inst):
	x,y = startcoords
	

	for i in inst:
		tx,ty = x,y

		match i:
			case "U":
				ty -= 1
			case "D":
				ty  += 1
			case "L":
				tx -= 1
			case "R":
				tx += 1
		if tx < 0 or tx >= 3 or ty >= 3 or ty < 0:
	
			continue
		else:

			x,y = tx,ty


	return x,y,GRID[y][x]

		



def main(inp):
	x,y = 1,1
	ans = ""

	for i in inp:
		x,y,key = getkey((x,y),i)
		ans += str(key)
	return ans


	



print(main(parser()))

