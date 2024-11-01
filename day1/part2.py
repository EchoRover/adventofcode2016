

def parser():
	with open('inp.txt') as f:
		text = f.read()

	return text.split(", ")



def format_line(line):
	if line[0][0] == line[1][0]:
		linedir = "y"
		yval = [i[1] for i in line]
		xval = line[0][0]
		return  (((xval,min(yval)),(xval,max(yval)))),linedir

	else:
		linedir = "x"
		xval = [i[0] for i in line]
		yval = line[0][1]
		return  (((min(xval),yval),(max(xval),yval))),linedir
	



def intersect(l1,l2):


	if l1[1] == l2[0]:
		return False,None

	l1,d = format_line(l1)
	l2,d2 = format_line(l2)
	if d == d2:
		return False,None

	if d == "y":
		vertical = l1
		horizontal = l2
	else:
		horizontal = l1
		vertical = l2
	

	if horizontal[0][0] <= vertical[0][0] <= horizontal[1][0]:
		if vertical[0][1] <= horizontal[0][1] <= vertical[1][1]:
			# print(horizontal,vertical)
			point = (vertical[0][0],horizontal[0][1])
			return True ,point

	# print(horizontal,vertical)
	return False,None


	# assume l2 divide line one
	#no diagonal only vertical and horizontal

	#vertically



# print(intersect(((0,0),(4,0)),((3,-8),(3,10))))


def main(inp):
	x = y = 0
	current_direction = 1

	locations = set()

	# north south east west
	# 1       2    3    4

	directionR = {1:3,2:4,3:2,4:1}
	directionL = {3:1,4:2,2:3,1:4}



	for i in inp:
		tx,ty = x,y

		
		

		

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

		new = ((tx,ty),(x,y))

		for j in locations:
			if intersect(j,new)[0]:
				point = intersect(j,new)[1]
				# print(point)
				
				return sum(map(abs,point))
		else:
			locations.add(new)




	return abs(x) + abs(y)



print(main(parser()))

