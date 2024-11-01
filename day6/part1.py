

import math

def parser():
	with open('inp.txt') as f:
		text = f.read()

	return text.split("\n")

def getmostcommon(messages):
	dict = {i:{} for i in range(len(messages[0]))}
	
	for message in messages:


		for index,char in enumerate(message):
			if char not in dict[index]:
				dict[index][char] = 1
			
			else:
				dict[index][char] += 1

	
	answer = [max(dict[i],key = lambda x : dict[i][x]) for i in dict]


	return "".join(answer)

def main(inp):
	
	return getmostcommon(inp)



print(main(parser()))

