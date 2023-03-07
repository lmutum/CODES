import random
def name():
    n = 5

    name = "D"

    for i in range(n):
        x = random.choice('abcdefghijklmnopqrstuvwxyz')
        name = name + x
    return name

i =1
name_list =[]
while i <100:
    x = name()
    name_list.append(x)
    i+=1


print(name_list)