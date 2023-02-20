import math
n=int(input("Enter your number: "))
m = int(math.sqrt(n))
flag = False
for i in (2,m+1):
    if (n%i == 0):
        flag = False
        break
    else:
        flag = True
if (flag):
    print(f"The given number {n} is a Prime number.")
else:
    print(f"The given number {n} is not a prime number.")
        