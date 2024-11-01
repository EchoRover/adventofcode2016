

import math

def parser():
	with open('inp.txt') as f:
		text = f.read()

	return text.split("\n")


GRID = [["x","x",1,"x","x"],["x",2,3,4,"x"],[5,6,7,8,9],["x","A","B","C","x"],["x","x","D","x","x"]]

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
		try:
			if min(tx,ty) < 0:
				continue
			a = GRID[ty][tx]
			if a == 'x':
				continue
		except:
			continue
		else:

			x,y = tx,ty


	return x,y,GRID[y][x]

		



def main(inp):
	x,y = 0,2
	ans = ""

	for i in inp:
		x,y,key = getkey((x,y),i)
		ans += str(key)
	return ans


	



print(main(parser()))

