import random

L = []
for i in range(30):
    L.append(random.randint(1,366))
    L.sort()
print(L)
i = 0
flag = 0
while i <= len(L)-2:
    if L[i]==L[i+1]:
        print("Repeats at :",L[i],"-",L[i+1])
        flag = 1
        
    i = i+1
          

if (flag == 0):
    print("Doesnt Repeats")
