#find out the minimum most element in the list l
#append that to a new list x
#remove the minimum from the original list l
# get mini from a function

def min_list(l):
    mini = l[0]
    for i in range(len(l)):
        if l[i]<mini:
            mini = l[i]

    return mini

def obvious_sort1(l):
    x = []
    while (len(l)>0):
        mini = min_list(l)
        x.append(mini)
        l.remove(mini)
    return x

l = [23,32,5,6,7,64,2,0]

print(obvious_sort1(l))


#breaking our problem into smaller modules and solving them makes it easy on our mind