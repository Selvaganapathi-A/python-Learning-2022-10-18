value = int(input("Enter number to Test:"))

isPrime = False

if value < 2:
    isPrime = False
elif value == 2:
    isPrime = True
elif value == 3:
    isPrime = True
else:
    isPrime = True
    for i in range(2, value):
        print(i)
        if (value % i) == 0:
            isPrime = False
            break
if isPrime:
    print("Given Number is Prime Number.")
else:
    print("Given Number is not Prime Number.")
