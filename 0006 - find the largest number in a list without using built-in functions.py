n = int(input("Number of Elements in list : "))

print("Enter Numbers:")

values = []

for i in range(n):
    values.append(int(input()))

largestNumber = values[0]

for val in values[1:]:
    if val > largestNumber:
        largestNumber = val

print()
print(largestNumber)
