# recursion  ---> function inside a function

def sum_rec(n):
    if n == 1:
        return 1
    else:
        return n+sum_rec(n-1)
    

print(sum_rec(10))

#python lets you call the same function within the function.