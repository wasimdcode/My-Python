# Diplay Data in Given Format (25 letters) 
#this made by me i know it is complicated 
item = input('Enter product Name -> ')
price = input('Enter Cost of Product -> ')
s = item + price
m = 25 - len(s)
d = item.ljust(m + len(price),'.')
print(d + price, len(d + price))
# short approach By Sir 
'''item = input('Entr The Item -> ')
price = input('Enter price -> ')
total_len = len(item) + len(price)
dots = '.' * (25 - total_len)
print(item+dots+price)'''