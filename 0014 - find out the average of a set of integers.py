n = int(input("Enter Number of Elements in set : "))
print("Enter Numbers : ")
values = set()

for _ in range(n):
    values.add(int(input()))

no = len(values)
sum_Of_Values = 0

for x in values:
    sum_Of_Values += x

print(sum_Of_Values / no)
