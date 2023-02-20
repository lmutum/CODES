n=int(input("Enter your number: "))
sum = 0
for i in range(n,0,-1):
    sum = sum + i
print("The sum of the first",n,"natural numbers is ",sum)