# This will Change Decimal to Binary
n = int(input("Enter Decimal Number"))
bin = ""
while n > 0:
    r = n % 2 
    n = n // 2
    bin = str(r) + bin

print(bin)
