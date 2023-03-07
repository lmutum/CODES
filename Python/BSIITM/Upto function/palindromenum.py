# check whether the entered number is a palindrome or not

n = int(input("Enter your number: "))
n2 = n
n1=abs(n)
n3 = n2
if (n>= 0):
    rev = n%10
    n = n//10
    while (n>0):                                    # we reversed the given number and checked whether 
        r = n%10                                    # the reversed number is same to the original number
        n = n//10
        rev = rev*10 + r
   
    if (n2 == rev):
        print("Its a palindrome")
    else:
        print("Its not a palindrome")
else:
    rev = n1%10
    n1 = n1//10
    while (n1>0):
        r = n1%10
        n1 = n1//10
        rev = rev*10 + r
    rev1 = rev - 2*rev

    if (n3 == rev1):
        print("Its a palindrome")
    else:
        print("Its not a palindrome")