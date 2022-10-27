days = int(input("enter days : "))
print(f'months contain {days} days are :')
if days == 28:
    print('feb')
elif days == 29:
    print('feb')
elif days == 30:
    print(('apr', 'jun', 'sep', 'nov'))
elif days == 31:
    print(('jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec'))
