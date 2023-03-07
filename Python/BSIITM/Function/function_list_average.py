# average of a list using function

def average(l):
    sum = 0
    for i in range(len(l)):
        sum = sum + l[i]
    avg = sum /len(l)
    return avg


l = [1,2,3,4,5,6,7,8,9]
print(average(l))