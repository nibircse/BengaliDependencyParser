#!/bin/bash
usage() { echo "Usage: $0 <train_file>"
	exit 1;
}
TRAIN_FILE=$1
if [ -z $TRAIN_FILE ];
then
	usage;
	exit 1;
fi



cp -r models/LATEST/* models/PREVIOUS #copying the previous
rm -rf models/LATEST
time_stamp=$(date +"%m-%d-%Y:%H:%M:%S")
DIR_NAME=models/$time_stamp/
ln -s  `pwd`/models/$time_stamp `pwd`/models/LATEST

mkdir -p $DIR_NAME

#Train a Basic model
echo "Training a basic model"
BASIC_MODEL_NAME=basic.model
#./TurboParser --train --file_train=$1 --file_model=$DIR_NAME/$BASIC_MODEL_NAME  --prune_basic=false --model_type=basic #--logtostderr
./TurboParser --train --file_train=$1 --file_model=$DIR_NAME/$BASIC_MODEL_NAME  --model_type=basic #--logtostderr

echo "Done training a basic model"

#Train a standard model
echo "Training a standard model"
STANDARD_MODEL_NAME=standard.model
./TurboParser --train \
	 --file_train=$1 \
	--file_model=$DIR_NAME/$STANDARD_MODEL_NAME \
	#--logtostderr
echo "Done training a standard model"

echo "Training a full model"
FULL_MODEL_NAME=full.model
./TurboParser --train \
	 --file_train=$1 \
	--file_model=$DIR_NAME/$FULL_MODEL_NAME \
	--model_type=full
	#--logtostderr
echo "Done training a full model"
