import sys

def parseCoNLLFile():
	with open('../Train/First Batch/trainA.txt.conll.coarsepostagged','w') as f:
		with open('../Train/First Batch/trainA.txt.conll') as file:
			lines = file.readlines()
		sentence_counter = -1
		for line in lines:
			line = line.strip()
			if len(line) != 0:
				words = line.split('\t')
				words[3] = words[4][0] #first letter of the POS tag
				print words[3]
				counter = 0;
				for word in words:
					if counter != len(words) -1:
						f.write(word+"\t")
					else:
						f.write(word+"\n")
					counter = counter + 1
	


parseCoNLLFile()