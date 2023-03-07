#finding the minimum item in a list
def list_min(l):
    mini = l[0]
    for i in range(len(l)):
        if (l[i]<mini):
            mini = l[i]
    return mini

l = [1,2,3,5,2,9,0,-1]

print(list_min(l))

def list_max(l):
    max = l[0]
    for i in range(len(l)):
        if (l[i]>max):
            max = l[i]
    return max

print(list_max(l))