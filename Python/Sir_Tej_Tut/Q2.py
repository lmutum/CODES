a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

#max = a
if a>b:
    if a>c:
        max = a
    else:
        max = c
else:
    if b>c:
        max = b
    else:
        max = c

print("The largest number is ",max)