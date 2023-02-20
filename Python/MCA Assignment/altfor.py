n=int(input("Enter your number: "))
sum1=sum2=sum=0
for i in range(1,n+1):
    if i%2==0:
        sum1=sum1+i
        print("-",i,end=" ")
    if i%2!=0:
        sum2=sum2+i
        print(i,end=" ")
    else:
        if i==n:
            break
        print("+",end=" ")
sum=sum2-sum1
print("=",sum)
    
    