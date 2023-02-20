#Create a list and perform the following methods: 1) insert() 2) remove() 3) append() 4) len() 5) pop() 6) clear()

List = []
n=int(input("Enter number of elements: "))
for i in range(0,n):
    element=input("Enter your elements: ")

# 1) Using insert()  -----> The insert() method inserts the specified value at the specified position.

    List.insert(i,element)
print(List)

#2) Using remove() -------> It removes the first occurrence of the object from the list

try:
    rem_element = input("Enter the element you want to remove from the list: ")
    List.remove(rem_element)
    print("The new list is: ",List)
except:
    print("------------------The element you are trying to remove is not present in the list---------------")

# 3) Using append() ----------> Python’s append() function inserts a single element into an existing list.
#  The element will be added to the end of the old list rather than being returned to a new list.
#  Adds its argument as a single element to the end of a list

App_element = input("Enter the element you want to append in the list: ")
List.append(App_element)
print("The appended list is ",List)

# to append another list in the existing list we use extend() instead of append()

# 4) Using len() --------------> returns the number of items in an object

length = len(List)
print("The number of elements in the list is ",length)

# 5) Using pop() ------------------> Optional. A number specifying the position of the element you want to remove,
#  default value is -1, which returns the last item

position = int(input("Enter the position of the element you want to remove: "))
if (position< length):
    removed_element = List.pop(position)
    print("The removed element from the list is: ",removed_element)
    print("The post pop list is :",List)
else:
    print("******** The element you are trying to remove is not present in the position you entered ******* ")
print("After operation of default pop(), the new list is : ")

#Default pop() is pop(-1) i.e it removes the last element from the list

List.pop()
print(List)

# Using clear() -------------> removes all the elements from a list

List.clear()
print("The cleared list has no parameters inside it.")
print(List)