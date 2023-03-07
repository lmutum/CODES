# a program to find the sum of first n natural numbers using for loop

n = int(input("Enter your number: "))

sum = 0
if (n>=0):
    for i in range(1,n+1):
        sum = sum + i
    print("Sum = ",sum)
else:
    n = abs(n)
    for i in range(1,n+1):
        sum = sum + i
    sum = sum - 2*sum
    print( "Sum = ",sum)