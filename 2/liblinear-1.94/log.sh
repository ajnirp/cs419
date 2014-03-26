#!/bin/bash

TRAIN="./train -s 0 -B 1 -c"
PREDICT="./predict"
CONVERT="./convert"

make
make convert

$CONVERT iris.data.training.txt > iris.data.training.liblinear
$CONVERT iris.data.validation.txt > iris.data.validation.liblinear

hyperparameters=(0.001 0.01 0.1 1 10 100 1000)
for i in "${hyperparameters[@]}"
do
	$TRAIN $i iris.data.training.liblinear
	$PREDICT iris.data.training.liblinear iris.data.training.liblinear.model output-$i
done