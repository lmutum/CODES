n =int(input())
i =1
fact = 1
if n == 0:
    fact = 1
    print(fact)
elif n>0:
    while i<=n:
        fact = fact * i
        i = i+ 1
    print(fact)
else:
    print("invalid")