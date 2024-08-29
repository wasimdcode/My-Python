# this will find Maximum Number
N_of_n = int(input("Enter Number of Numbers"))
count = 0
max = int(input("Enter Number"))
while count < N_of_n - 1:
    n = int(input("Enter a Number"))
    if n > max:
        max = n
    count = count + 1

print("Maximum Number is", max)


