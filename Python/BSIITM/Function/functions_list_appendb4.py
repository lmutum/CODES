def list_appendbefore(l,z):
    new_list= []
    for i in range(len(z)):
        new_list.append(z[i])
    for j in range(len(l)):
        new_list.append(l[i])
    return new_list
    
l=[1,2,3,4,5]
z= [7,6,8,9,0]
print(list_appendbefore(l,z))