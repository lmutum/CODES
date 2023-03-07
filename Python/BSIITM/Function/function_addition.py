def sum(a,b):
    s = a+b
    return s


sum(3,4)

def discount(cost,d):
    dis = cost - (cost*0.01*d)
    return dis

print(sum(6,4) + discount(2000,10))