n=int(input("Enter your number: "))
sum=0
i=1
while i <= n:
    sum = sum + i
    print(i,end="")
    if i == n:
        break
    print("+",end="")
    i=i+1
print(" = ",sum)

