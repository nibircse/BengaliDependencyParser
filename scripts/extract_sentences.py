import sys
#split the string on <s> and </s> and add a . at the end
with open('out.txt.bak') as file:
	text = file.read()
#text=text.decode("utf-8")
print text
#lines = text.split("\n") #each line of the text

#for line in lines:
#	print line
	#line = line.replace("<s> ","")
	#segments = line.split("</s>")
	#print segments[0]+"."
