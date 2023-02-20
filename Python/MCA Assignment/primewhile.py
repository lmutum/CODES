n = int(input("Enter your number: "))
i =2
if n>0:
    if n == 1:
        print("The given number 1 is \x1B[3m not \x1B[0m a prime number")
    elif n == 2 or n == 3:
        print (f"The given number {n} is a \x1B[3m prime number \x1B[0m ")
    else:
        while i <= n/2:
            if n%i==0:
                print(f"The given number {n} is \x1B[3m not \x1B[0m a prime number")
                break
            else:
                print(f"The given number {n} is a \x1B[3m prime number \x1B[0m")
                break
            i = i +1
else:
    print(f"The given number {n} is \x1B[3m not \x1B[0m a prime number")