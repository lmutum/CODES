n=int(input("Enter Number: "))
n1 = 0
n2 = 1
i =1
if n == 0:
    print(f"The first {n} Fibonaci series are :")
else:
    print(f"The first {n} Fibonaci series are :" , end=" ")
    print(n1,end=" ")
    while i < n:
        print(n2,end=" ")
        n3= n1+n2
        n1 = n2
        n2 = n3
        i = i + 1