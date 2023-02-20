# A program to check whether a word is a palindrom or not

string = str(input("Enter your word:"))
length =len(string)
flag = False

for i in range(0,length):
    print(string[i])
    print(string[:-i])
    if (string[i]==string[:-i]):
        flag = True
    else:
        flag = False
if (flag == True):
    print("Palindrom")
else:
    print("Not Palindrom")
