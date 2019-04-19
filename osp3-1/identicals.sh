read -p "Do you want to continue?" reply
if [[ $reply = "y" ]]; then
	echo "You entered " $reply
fi

read -p "Do you want to continue?" reply
if [ $reply = "y" ]; then
	echo "You entered " $reply
fi

read -p "Do you want to continue?" reply
if test $reply = "y";  then
	echo "You entered " $reply
fi

