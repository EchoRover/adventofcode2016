import os

MAINCODE = """

import math

def parser():
	with open('inp.txt') as f:
		text = f.read()

	return text.split()



def main(inp):
	pass



print(main(parser()))

"""

def createfile(basename):
	basename = "day" + basename
	try:
		os.mkdir(basename)
	except:
		print(f"dir {basename} already exists")

	f = open(basename + '/part1.py',"w").write(MAINCODE)
	f = open(basename + '/part2.py',"w").write(MAINCODE)
	f = open(basename + '/inp.txt',"w")






createfile('7')



