#Find the largest number from a given set of n numbers
n = int(input("Enter number of given numbers: "))
list = []
for i in range(n):
    x = int(input("Enter your number: "))
    list.append(x)
list.sort()


print("The maximum of the numbers is ",list[-1])