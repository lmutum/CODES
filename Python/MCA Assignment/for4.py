rows =int(input("Enter number of rows: "))
for i in range(1,rows+1):
    print(i,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
    