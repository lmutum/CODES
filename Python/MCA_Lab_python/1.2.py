# Create a dictionary and apply the following methods 
# 1) print the dictionary items 2) access items 3) useget() 4) change values 5) use len()

Dictionary = {}

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates. -----[key:value]

Dictionary = dict(Manipur = "Imphal", Population = 2855794, Census = 2011, Literacy = '76.94%', Sex_ratio =985 )
print("The Dictionary is : ", Dictionary) # printing the Dictionary

# Accessing Items in Dictionary is done by  referring to its key name, inside square brackets

print("The available keys are : \"Manipur\" , \"Polpulation\" , \"census\" , \"Literacy\" , \"sex_ratio\"")
flag = 0
while (flag != 1):
    key = input("Enter your preferred key: ")
    if key in Dictionary:
        item = Dictionary[key]
        print(item)
        flag = 1
    else:
        print("The key you entered doesn't exists in the Dictionary.")
        print("Do you want to enter again , if yes press 1 !!!")
        hit = input()
        if (hit == "1"):
            flag = 0
        else:
            flag = 1

# use get() --------------> returns the value of the item with the specified key

print("The available keys are : \"Manipur\" , \"Polpulation\" , \"Census\" , \"Literacy\" , \"Sex_ratio\"")

flag_get = 0
while (flag_get != 1):
    key_get = input("Enter your preferred \"get\" key: ")
    if key_get in Dictionary:
        item_get = Dictionary.get(key_get)
        print(item_get)
        flag_get = 1
    else:
        print("The key you entered doesn't exists in the Dictionary.")
        print("Do you want to enter again , if yes press 1 !!!")
        hit_get = input()
        if (hit_get == "1"):
            flag_get = 0
        else:
            flag_get = 1


# change values in Dictionary
#To insert new keys/values into a Dictionary, use the square brackets and the assignment operator.
#  With that, the update() method can also be used. 
# Remember, if the key is already in the dictionary, its value will get updated, else the new pair gets inserted.
# Dictionary.update({"Grade":"A","Tax":"Yes"})


flag_change = 0
while (flag_change != 1):
    key_change = input("Enter the key you want to \"change\": ")
    print("Old value of ",key_change, "is", Dictionary[key_change])
    Value_change = input("Enter the new value: ")
    if key_change in Dictionary:
        Dictionary[key_change] = Value_change
        print("The Changed dictionary is: ",Dictionary)
        flag_change = 1
    else:
        print("The key you entered doesn't exists in the Dictionary.")
        print("Do you want to enter again , if yes press 1 !!!")
        hit_change = input()
        if (hit_change == "1"):
            flag_change = 0
        else:
            flag_change = 1

# Using len() --------------> returns the number of keys in python dictionary

dict_length = len(Dictionary)
print("The number of keys in the present dictionary is ", dict_length)

