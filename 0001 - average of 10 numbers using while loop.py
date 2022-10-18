# Average of 10 Numbers

nos = (6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

length = len(nos)
i = 0

sumOfNumbers = 0
while i < length:
    sumOfNumbers = sumOfNumbers + nos[i]
    i = i + 1

average = sumOfNumbers / length

print(average)
