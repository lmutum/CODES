n=int(input("Enter your number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print(i,end="")
    if i==n:
        break
    print("+",end="")
print('=',sum)