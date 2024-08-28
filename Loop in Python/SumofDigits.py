# it will Calculate Sumo of Digts
n = int(input("Enter A Number"))
sum = 0
while n > 0:
    r = n % 10
    n = n // 10
    sum = sum + r

print("The sum of Number is", sum)