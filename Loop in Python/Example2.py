# it will work on Condition until It's True
n = int(input("Enter Number"))
while n > 0:
    r = n % 10
    n = n // 10
    print(r)
