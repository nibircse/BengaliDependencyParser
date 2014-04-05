import sys

def parseCoNLLFile():
	with open('../Train/all/train.txt.conll.blanklines','w') as f:
		with open('../Train/all/train.txt.conll') as file:
			lines = file.readlines()
		sentence_counter = -1
		for line in lines:
			line = line.strip()
			if len(line) != 0:
				words = line.split('\t')
				if words[0] == '1':
					f.write('\n')
				counter = 0;
				for word in words:
					if counter != len(words) -1:
						f.write(word+"\t")
					else:
						f.write(word+"\n")
					counter = counter + 1


parseCoNLLFile()