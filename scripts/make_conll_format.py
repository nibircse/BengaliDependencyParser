with open('../Test/Third Batch/test_dataset_C.txt') as file:
	text = file.read()

lines = text.split("\n") #each line of the text

for line in lines:
	words = line.split();
	word_counter = 1
	for word in words:
		print str(word_counter)+"\t"+word+"\t"+word+"\t"+"NON"+"\t"+"NON"+"\t"+"NON|NON"+"\t"+str(word_counter)+"\t"+"_"+"\t"+"_"+"\t"+"_"
		word_counter = word_counter + 1
	print "\n"
