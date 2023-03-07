def comp(p,r,t):
    c = 1 + r/100
    if t==1:
        return p*c
    else:
        return comp(p,r,t-1)*c
    
print(comp(2000,10,3))
