#!/bin/bash

cp ../first_batch/trainA.txt.conll .
cp ../second_batch/trainB.txt.conll .
cp ../third_batch/trainC.txt.conll .
cp ../fourth_batch_last/trainD.txt.conll .

cat trainA.txt.conll > train.txt.conll
cat trainB.txt.conll >> train.txt.conll
cat trainC.txt.conll >> train.txt.conll
cat trainD.txt.conll >> train.txt.conll
cd ../../scripts/

#sanitize the conll
sh sanitize_conll.sh ../Train/all/train.txt.conll
