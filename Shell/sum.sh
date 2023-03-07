#!bin/bash
#read the user input
echo "Enter your first number: "
read first_num

echo "Enter your second number: "
read second_num

sum=$(( $first_num + $second_num ))

echo " The sum of the two number is $sum"