s1 = float(input("Enter Side1 Length :"))
s2 = float(input("Enter Side2 Length :"))
s3 = float(input("Enter Side3 Length :"))

s = (s1 + s2 + s3) / 2

area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5

print(area)
