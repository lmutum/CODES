#Find the largest number from a given set of n numbers
n = int(input("Enter number of given numbers: "))
list = []
for i in range(n):
    x = int(input("Enter your number: "))
    list.append(x)

largest= list[0]
where = 0

for i in range(1,n):
    if largest<list[i]:
        largest = list[i]
        where = i

print("The largest number is ",largest , "and is found in position", where)