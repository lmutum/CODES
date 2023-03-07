def fibo(n):
    if n==1 or n==2:
        return 1
    x = fibo(n-1) + fibo(n-2)
    return x

print(fibo(3))