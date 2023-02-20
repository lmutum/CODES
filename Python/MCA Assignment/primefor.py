n = int(input("Enter your number: "))
if n>0:
    if n == 1:
        print("The given number 1 is \x1B[3m not \x1B[0m a prime number")
    elif n == 2 or n == 3:
        print (f"The given number {n} is a \x1B[3m prime number \x1B[0m ")
    else:
        for i in range(2,int(n/2+1)):            # n/2 +1 is taken to include the range when n is 4 and 5
            if n%i==0:
                print(f"The given number {n} is \x1B[3m not \x1B[0m a prime number")
                break
            else:
                print(f"The given number {n} is a \x1B[3m prime number \x1B[0m")
                break
else:
    print(f"The given number {n} is \x1B[3m not \x1B[0m a prime number")