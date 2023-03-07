import math
flag = 0
n = int ( input())
if n < 2:
    flag = 0
elif n==5 or n==7 or n ==2:
    flag = 1
else:
    if n % 2 ==0:
        flag = 0
    else:
        for i in range(3,int(math.sqrt(n))+1,2):
            if n%i == 0:
                flag = 0
            else:
                flag = 1
if flag == 1:
    print("prime")
else:
    print("Not prime")