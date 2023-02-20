n=int(input("Enter number:"))
abs_num = abs(n)
if (n >= 0):
    rev = n % 10
    n =n //10
    while (n>0):
        r = n%10
        n = n//10
        rev = rev*10 + r
    print(rev)
else:
    rev = abs_num%10
    abs_num = abs_num//10
    while(abs_num>0):
        r = abs_num%10
        abs_num = abs_num//10
        rev = rev*10 + r
    print(rev - 2*rev)