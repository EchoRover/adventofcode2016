

def parser():
	with open('inp.txt') as f:
		text = f.read()

	return text.split(", ")





def main(inp):
	x = y = 0
	current_direction = 1

	locations = set()

	# north south east west
	# 1       2    3    4

	directionR = {1:3,2:4,3:2,4:1}
	directionL = {3:1,4:2,2:3,1:4}



	for i in inp:
	

		
		

		

		cdir = i[0]
		move = int(i[1:])
		if cdir == "R":
			current_direction = directionR[current_direction]
		else:
			current_direction = directionL[current_direction]

		match current_direction:
			case 1:
				y += move
			case 2:
				y -= move
			case 3:
				x += move
			case 4:
				x -= move

	




	return abs(x) + abs(y)



print(main(parser()))

