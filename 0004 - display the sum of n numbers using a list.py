n = int(input("Enter number of elements to Count : "))
values = []

for i in range(n):
    values.append(int(input()))

sumOfNumbers = 0

for val in values:
    sumOfNumbers += val

print(sumOfNumbers)
