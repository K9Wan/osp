#!/bin/bash
if test -w "$1"
	then
	echo "file $1 is write-able"
else
	echo "file $1 is not write-able"
fi
