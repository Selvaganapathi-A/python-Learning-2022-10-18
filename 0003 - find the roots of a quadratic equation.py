a = int(input("Value of a : "))
b = int(input("Value of b : "))
c = int(input("Value of c : "))

root1 = (-b + (((b**2) - (4 * a * c)) ** 0.5)) / (2 * a)
root2 = (-b - (((b**2) - (4 * a * c)) ** 0.5)) / (2 * a)

print((root1, root2))
