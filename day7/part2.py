

import math

def parser():
	with open('inp.txt') as f:
		text = f.read()

	return text.split("\n")


			

def isaba(text,check = None):
	listaba  = []
	listrev = []
	for i in range(0,len(text) - 2):
		if text[i] == text[i + 1]:
			continue

		if text[i] == text[i + 2]:
			tt = (text[i:i + 3])

			if check is not None and tt in check:
				return True

			listrev.append(text[i + 1] + text[i] + text[i + 1])

	if check is not None:
		return False
			

	return listrev



def isabba(text):

	for i in range(0,len(text) - 3):
		if text[i] == text[i + 1]:
			continue

		if text[i:i + 2] == text[i + 3:i + 1:-1]:
			return True

	return False
			



def support_ssl(code):

	abba = []
	hypernet = []
	text = ""
	ishyper = False
	for i in code:
		if i == "[":
			ishyper = True
			abba.append(text)
			text = ""

		elif i == "]":
			ishyper = False
			hypernet.append(text)
			text  = ""
		else:
			text += i 
	if text:
		abba.append(text)

	codes = []

	for i in abba:
		codes.extend(isaba(i))

	if not codes:
		return

	if any([isaba(i,codes) for i in hypernet]):
		return True
	

	
	return False






def main(inp):
	return sum([1 if support_ssl(i) else 0 for i in inp ])



print(main(parser()))

