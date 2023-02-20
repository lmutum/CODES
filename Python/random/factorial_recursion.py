# python program to find the factorial of a number using recursion

n = int(input())


def fac(n):
    if ((n == 1) or (n ==0)):
        return 1
    elif(n< 0):
        return "invalid"
    else:
        n = n*fac(n-1)
        return n


print(f"The factorial of {n} is {fac(n)}")