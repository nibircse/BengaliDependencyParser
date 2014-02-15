with open('../Test/MS_POS_tagged_raw.txt') as file:
	text = file.read()
#print text
lines = text.split("\n") #each line of the text

for line in lines:
	words = line.split()
	print words
# 	s=""
# 	for word in words:
# 		ben = word.split("_")
# 		s = s +" "+ben[0]
# 	print s
