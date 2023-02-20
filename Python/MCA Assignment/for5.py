rows =int(input("Enter number of rows: "))
for i in range(1,rows+1):
    for k in range(1,2*(rows-i)+1):
        print(end=" ")
    for l in range(1,i):
        print(l,end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()