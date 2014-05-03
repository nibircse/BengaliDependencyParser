BengaliDependencyParser
=======================
This is implementation of a dependency parser of the language Bengali. This repository contains a dataset of around 7500 annotated tokens of Bengali Text. For the annotation decisions (and caveats) please refer the report. 

Contents

Data/ - Contains the annotated dataset. All the files are in CoNLL format.

Data/Train - The training set (total of 5463 tokens annotated)
Data/Train/train.txt.conll - the annotated train file

Data/Test/TestA/testA.conll - the annotated test file
Data/Test/TestA/testB.conll - the annotated test file

To run the parser:

You can use your own training data or use the one shared my me. To run do the following.
 cd TurboParser-2.1.0.

Train script: ./run_train.sh <path to train file>

Test script : ./run_test.sh <path to test file>

It will run all the 3 (basic, standard and full models) of Turbo Parser. The labelled/unlabelled accuracy will be printed on the console after the test script is run.

Thanks!


