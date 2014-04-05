#!/bin/bash

FILE=$1

sed -i.bak 's/,\\SEN //g' $1
sed -i.bak 's/-\\SEN //g' $1
sed -i.bak 's/"\\SEN //g' $1
sed -i.bak 's/:\\SEN //g' $1
sed -i.bak "s/'\\SEN //g" $1
