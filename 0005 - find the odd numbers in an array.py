numbers = []

count = int(input("How many Numbers you want to have in list : "))

for i in range(count):
    numbers.append(int(input()))


oddNumbers = []

for number in numbers:
    if (number % 2) == 1:
        oddNumbers.append(number)

print(oddNumbers)
