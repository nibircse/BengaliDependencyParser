file_conll=$1
awk '{ if (NF>0) print $2 "\t" $5; else print ""}' ${file_conll} > ${file_conll}.tagging
