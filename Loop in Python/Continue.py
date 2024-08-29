# this is the Example of Continue
count = 0
while count < 10:
    n = int(input("Enter A Number"))
    count += 1
    if n % 3 == 0:
        continue #this will repeat condition when it's true and will not go to next line
    print(n)
