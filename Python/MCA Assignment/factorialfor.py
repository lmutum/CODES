n=int(input("Enter your number: "))
fac = 1
if n>=0:
    for i in range(n,1,-1):
        fac = fac * i
    print(f"The factorial of the given number {n} is ",fac)
else:
    print("You are trying to find factorial of a negative integer, Please enter a positive integer")