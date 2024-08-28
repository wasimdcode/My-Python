# this will count How many Digits in input
n = int(input("Enter a Number"))
count = 0
while n > 0:
    n = n // 10
    count += 1
print('Number of Digits are', count)