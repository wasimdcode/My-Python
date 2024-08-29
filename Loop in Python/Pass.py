# this is the Example of Pass
count = 0
while count < 10:
    n = int(input("Enter A Number"))
    if n % 3 == 0:
        pass # it will do nothing and I can change Logic == to != instead of using Pass
    else:
        print(n)
    count += 1