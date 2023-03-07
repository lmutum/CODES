#find out the minimum most element in the list l
#append that to a new list x
#remove the minimum from the original list l

def obvious_sort(l):

    x = []
    while len(l) > 0:
        mini = l[0]
        for i in range(len(l)):
            if l[i]<mini:
                mini = l[i]
        x.append(mini)
        l.remove(mini)
    return x

l = [29,3,4,2,1,332,90]

print(obvious_sort(l))