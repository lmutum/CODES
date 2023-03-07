# write a python program using functions which calculates the number of upper case letters,
#lower case letters , total number of characters and number of words.

def upper(words):
    up = 0
    for c in words:
        if (c.isupper()):
            up+=1
    return up

def lower(words):
    low = 0
    for c in words:
        if (c.islower()):
            low +=1
    return low


def characters(words):
    cha = 0
    for c in words:
        cha = cha + 1
    return cha

def word_c(words):
    count = 1
    for c in words:
        if c == ' ':
            count+=1
    return count




words = input("Enter your words: ")
print(upper(words))
print(lower(words))
print(characters(words))
print(word_c(words))