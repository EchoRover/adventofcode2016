

import math

def parser():
	with open('inp.txt') as f:
		text = f.read()

	return text.split("\n")



def isabba(text):

	for i in range(0,len(text) - 3):
		if text[i] == text[i + 1]:
			continue

		if text[i:i + 2] == text[i + 3:i + 1:-1]:
			return True

	return False
			



def support_tls(code):

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

	if any([isabba(i) for i in abba]) and  all([not isabba(i) for i in hypernet]):
		return True
	return False






def main(inp):
	return sum([1 if support_tls(i) else 0 for i in inp ])



print(main(parser()))

