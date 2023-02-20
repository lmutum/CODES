n=int(input("Enter Number:"))
i=1
sum1 = sum2 = sum = 0
while i<=n:
    if i%2==0:
        sum1=sum1+i
        print('-',i,end=" ")
    if i %2!=0:
        sum2=sum2+i
        print(i,end=" ")
    else:
        if i == n:
            break
        print("+",end=" ")
    i=i+1
sum=sum2-sum1
print('=',sum)