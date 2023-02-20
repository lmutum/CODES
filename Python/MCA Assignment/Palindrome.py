m = int (input( "Enter Number: "))
n =m
sum = 0
while m!=0:
    r = m % 10
    sum = sum *10 + r
    m = int (m/10)
print(sum)
if n == sum:
    print( "The given number", n,"is a pallindrom")
else:
    print( "The given number", n ,"is not a pallindrom")