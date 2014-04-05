with open('../Train/third_batch/trainc.txt') as file:
	text = file.read()

lines = text.split("\n") #each line of the text

for line in lines:
	words = line.split();
	word_counter = 1
	for word in words:
		 word_POS = word.split("\\")
		 actual_word = word_POS[0]
		 POS = word_POS[1]
		 coarse_pos  = POS[0]
		 print str(word_counter)+"\t"+actual_word+"\t"+"_"+"\t"+coarse_pos+"\t"+POS+"\t"+"NON|NON"+"\t"+str(word_counter)+"\t"+"_"+"\t"+"_"+"\t"+"_"
		 word_counter = word_counter + 1
		#I tried removing the new line -- it doesnt work
	print "\n"
