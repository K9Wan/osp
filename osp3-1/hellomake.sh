#!/bin/bash
COUNTER=0
while [ $COUNTER -lt 10 ]
do
	touch "hello.$COUNTER.txt"
	echo The counter is $COUNTER
	let COUNTER=$COUNTER+1
done
