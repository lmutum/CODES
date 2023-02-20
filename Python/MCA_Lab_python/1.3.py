# Create a tuple and perform the following methods
# 1) Add items 2) len() 3) check for item in tuple 4)Access items

# A tuple is a collection which is ordered and unchangeable.

Tuple =("Imphal-East", "Bishnupur", "Imphal-West", "Moirang", "Kakching")

print(Tuple)

# Tuple items are ordered, unchangeable, and allow duplicate values

# tuples only can be concatenated. It cannot be concatenated with other types such as list,sets etc

tuple_add = Tuple + (1,2,3)
print(tuple_add)

# using len()

length = len(Tuple)
print(length)

length= len(tuple_add)
print(length)


# checking tuple items are done through indexing as they are odered 

n = int(input("Input the index you want to check: "))
if ((n<length) and (n>0)):
    item = tuple_add[n]
    print(item)
else:
    print("The index you entered exceed the permissible length")
 
