# Write a program to create a menu with the following options
# 1. TO PERFORM ADDITITON 2. TO PERFORM SUBTRACTION
# 3. TO PERFORM MULTIPICATION 4. TO PERFORM DIVISION
# Accepts users input and perform the operation accordingly. Use functions with arguments.

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))

def addition(num1,num2):
    sum = num1 + num2
    return (sum)

def subtraction(num1,num2):
    subs = num1 - num2
    return(subs)

def mul(num1, num2):
    mul = num1 * num2
    return (mul)

def division(num1,num2):
    if (num2 != 0):
        div = num1/num2
        return(div)
    else:
        return ("invalid division")

print("Enter your choice for:  ")
print(" 1. TO PERFORM ADDITITON ")
print(" 2. TO PERFORM SUBTRACTION")
print(" 3. TO PERFORM MULTIPICATION")
print(" 4. TO PERFORM DIVISION")
choice = int(input())

if (choice == 1):
    print("The sum of the numbers is ",addition(num1,num2))

elif (choice == 2):
    print("The difference of the numbers is ",subtraction(num1,num2))

elif (choice == 3):
    print("The multiplication of the numbers is ",mul(num1,num2))

elif (choice == 4):
        
    if (num2 != 0):
        print("The division of the numbers is ",division(num1,num2))
    else:
        print("Invalid division")
         

else:
    print("You have entered an invalid choice.")


