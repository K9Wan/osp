#!/bin/bash
checkfile() {
	for file
	do
		if [ -f "$file" ]; then
			echo "$file is a file"
		else
			if [ -d "$file" ]; then
				echo "$file is a directory"
			fi
		fi
	done
}
checkfile . funtest hello.sh
