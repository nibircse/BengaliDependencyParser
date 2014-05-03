usage() { echo "Usage: $0 <test_file> [run_previous(r)]"
	        exit 1;
	}


TEST_FILE=$1
RUN_PREV=$2
if [ -z $TEST_FILE ];
then
	usage;
fi
LATEST_DIR=PREVIOUS
if [ -z $RUN_PREV ];
then
LATEST_DIR=LATEST
fi
echo "In the testing phase"

time_stamp=$(date +"%m-%d-%Y:%H:%M:%S")
pred_dir_name=data/test/predictions/$time_stamp/
rm -rf data/test/predictions/LATEST
mkdir -p $pred_dir_name
ln -s  `pwd`/$pred_dir_name `pwd`/data/test/predictions/LATEST

MODEL=basic
PREDICTED_FILE=$pred_dir_name/prediction.$MODEL
if [ -f models/$LATEST_DIR/$MODEL.model ];
then
echo "Testing with the Basic model"
./TurboParser --test \
	        --evaluate \
		        --file_model=models/$LATEST_DIR/$MODEL.model \
			        --file_test=$TEST_FILE\
				        --file_prediction=$PREDICTED_FILE \
#					        --logtostderr
scripts/eval.pl -b -q -g $TEST_FILE -s $PREDICTED_FILE | tail -5
echo "Done testing"
fi

MODEL=standard
PREDICTED_FILE=$pred_dir_name/prediction.$MODEL

if [ -f models/$LATEST_DIR/$MODEL.model ];
then
	
echo "Testing with the Standard model"
./TurboParser --test \
	      --evaluate \
	      --file_model=models/$LATEST_DIR/$MODEL.model \
	      --file_test=$TEST_FILE\
	      --file_prediction=$PREDICTED_FILE \
#	      --logtostderr

scripts/eval.pl -b -q -g $TEST_FILE -s $PREDICTED_FILE | tail -5
echo "Done testing (standard)"
fi

MODEL=full
PREDICTED_FILE=$pred_dir_name/prediction.$MODEL
if [ -f models/$LATEST_DIR/$MODEL.model ];
then

echo "Testing with the Full model"
./TurboParser --test \
	      --evaluate \
	      --file_model=models/$LATEST_DIR/$MODEL.model \
	      --file_test=$TEST_FILE\
	      --file_prediction=$PREDICTED_FILE \
#	      --logtostderr

scripts/eval.pl -b -q -g $TEST_FILE -s $PREDICTED_FILE | tail -5
echo "Done testing (full)"
fi
