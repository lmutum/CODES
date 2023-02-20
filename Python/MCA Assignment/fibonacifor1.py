n=int(input("Enter Number: "))
n1 = 0
n2 = 1
if n == 0:
    print(f"The first {n} Fibonaci series are :")
else:
    print(f"The first {n} Fibonaci series are :" , end=" ")
    #print(n1,end=" ")
    for i in range(1,n+1):
        print(n2,end=" ")
        n3= n1+n2
        n1 = n2
        n2 = n3