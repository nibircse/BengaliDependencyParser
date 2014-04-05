import sys

def parseCoNLLFile():
	with open('../Test/Third Batch/POSTagged/test_dataset_C.txt.postagged.lemma_removed','w') as f:
		with open('../Test/Third Batch/POSTagged/test_dataset_C.txt.postagged') as file:
			lines = file.readlines()
		sentence_counter = -1
		for line in lines:
			line = line.strip()
			if len(line) != 0:
				words = line.split('\t')
				print words
				words[2] = '_'
				counter = 0;
				for word in words:
					if counter != len(words) -1:
						f.write(word+"\t")
					else:
						f.write(word+"\n")
					counter = counter + 1
			else:
				f.write('\n')


parseCoNLLFile()