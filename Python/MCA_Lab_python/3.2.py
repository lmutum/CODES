# a python program to check whether the given string is palindrome or not.

string = str(input())
length = len(string)
flag = 0
for i in range(0,length):
   # print(string[i])
   # print(string[-(i+1)])
    if (string[i]==string[-(i+1)]):
        flag = 1
       # print(flag)
    else:
        flag = 0
      #  print(flag)
#print("final_flag = ",flag)
        
if (flag ==1):
    print("palindrom")
else:
    print("not palindrom")