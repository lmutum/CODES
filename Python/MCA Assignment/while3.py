rows=int(input("Enter number of rows: "))
i=1
while i <= rows:
    print (i,end=" ")
    j=i-1
    while j >0:
        print(j,end=" ")
        j = j-1
    i +=1
    print()
    