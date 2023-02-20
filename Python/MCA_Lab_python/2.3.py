# Write a python program to find largest number among three numbers.

# inputting the three numbers by the user
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter First Number: "))
num3 = int(input("Enter First Number: "))

#checking condition amongst the three numbers

if ((num1>num2) and (num1>num3)):
    print(f"The largest amonst the three given numbers {num1}, {num2} and {num3} is {num1}")
elif ((num2>num1) and (num2>num3)):
    print(f"The largest amonst the three given numbers {num1}, {num2} and {num3} is {num2}")
else:
    print(f"The largest amonst the three given numbers {num1}, {num2} and {num3} is {num3}")

