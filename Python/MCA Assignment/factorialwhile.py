n=int(input("Enter your number: "))
i = 1
Fac=1
if n>=0:
    while i <= n:
        Fac = Fac * i
        i=i+1
    print(f"The factorial of the given number {n} is ",Fac)
else:
    print("You are trying to find factorial of a negative integer, Please enter a positive integer")