# It will Sum Numbers
no = int(input("Enter How many Numbers You want to sum"))

sum = 0
count = 0
while count < no:
    n = int(input("Enter a Number"))
    sum = sum + n
    count = count + 1

print("The Sum is", sum)