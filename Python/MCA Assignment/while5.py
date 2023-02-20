rows=int(input("Enter number of rows: "))
i=1
while i <= rows:
    j=1
    while j <= 2*(rows-i):
        print(end=" ")
        j+=1
    j=1
    while j <=i:
        print (j, end=" ")
        j +=1
    j=i-1
    while j>0:
        print(j, end=" ")
        j-=1
    print()
    i+=1
i=4
while i>=1:
    j=1
    while j<=2*(rows-i):
        print(end=" ")
        j = j+1
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    j=i-1
    while j>0:
        print(j,end=" ")
        j-=1
    print()
    i -=1