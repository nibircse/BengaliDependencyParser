#read rhe POS tagged file
import sys

def parseCoNLLFile():
	with open('../Test/Third Batch/third_batch.conll') as file:
		lines = file.readlines()
	sentence_counter = -1
	parent_list = [] #higher level list -- each element is a line (which is a list)
	for line in lines:
		line = line.strip()
		if len(line) != 0:
			words = line.split('\t')
			if words[0] == "1": #new sentence in the test file
				if sentence_counter != -1:
					parent_list.append(curr_line_list)
				sentence_counter = sentence_counter + 1
				curr_line_list = []
			conll_token_list = []
			for conll_token in words:
				conll_token_list.append(conll_token)
			curr_line_list.append(conll_token_list)				
	return parent_list

def writeCoNLLFile(File):
	with open('../Test/Third Batch/POSTagged/test_dataset_C.txt.postagged','w') as f:
		for each_line in File:
			for each_word in each_line:
				f.write('\t'.join(str(conll_token) for conll_token in each_word)) 
				f.write("\n")
			f.write("\n")






#split the string on <s> and </s> and add a . at the end
with open('../Test/Third Batch/test_dataset_C.txt.postagged') as file:
	text_POS = file.read()


with open('../Test/Third Batch/test_dataset_C.txt') as file:
	text = file.read()

orig_lines = text.split("\n")
lines = text_POS.split("\n")
pos_counter = 0
line_nums = []
all_word_list = []
all_pos_list = []
for line in lines:
	line = line.strip()
	pos_words = line.split(" ")
	counter = 0
	pos_list = []
	word_list = []
	for words in pos_words:
		word_pos = words.split("\\")
		if len(word_pos)!=2:
			continue
		word = word_pos[0]
		#print "Word - "+word
		pos = word_pos[1]
		#print "Pos - "+pos
		if pos == 'SEN':
			if counter != len(pos_words) - 1: #This is a punctuation in the middle of the sentence
				#print "hi" 
				counter = counter + 1
				continue #ignoring this punct
		word_list.append(word)
		pos_list.append(pos)				
		counter = counter + 1
	match = False
	all_pos_list.append(pos_list)
	all_word_list.append(word_list)
	orig_line_counter = 0
	for orig_line in orig_lines:
		flag = 0
		match = False
		orig_line = orig_line.strip();
		orig_words = orig_line.split(" ");
		if len(orig_words) == len(word_list):
			for i in xrange(0,len(orig_words)):
				if orig_words[i][0].lower() != word_list[i][0].lower(): #This is not the same word, so probly wrong line
					flag = 1
					break
			if flag == 0: #we have an exact match,
				match = True
				print "Postagged line "+str(pos_counter)+" exact match for line" + str(orig_line_counter)
				line_nums.append((pos_counter,orig_line_counter))
		orig_line_counter = orig_line_counter + 1		
	pos_counter = pos_counter + 1
	doIt = True
	parent_list = parseCoNLLFile()
print len(parent_list)
#print parent_list[0]
#print line_nums
#print all_word_list
if doIt:
	for pair in line_nums:
		pos_line_num = int(pair[0])
		orig_line_num = int(pair[1])
		#get the POS lisr
		try:
			all_pos = all_pos_list[pos_line_num]
			orig_line = parent_list[orig_line_num]
			counter1 = 0;
			for conll_line in orig_line:
				conll_line[3] = all_pos[counter1][0]
				conll_line[4] = all_pos[counter1]
				counter1 = counter1 + 1
		except:
			print 'hi'
		#print orig_line
	#print parent_list
	writeCoNLLFile(parent_list)
