rows =int(input("Enter number of rows: "))
for i in range(1,rows+1):
    for k in range(1,2*(rows-i)+1):
        print(end=" ")
    for l in range(1,i):
        print(l,end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
for i in range(rows-1,0,-1):
    for j in range(1,2*(rows-i)+1):
        print(end=" ")
    for j in range(1,i):
       print(j,end=" ")
    for i in range(i,0,-1):
        print(i,end=" ")
    print()