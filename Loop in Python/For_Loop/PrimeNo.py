# This will Check value is Prime number or not
n = int(input("Enter a Number "))
count = 0
for i in range(1,n+1):
    if n % i == 0: #for Dividable or not
        count += 1 #for cheking value is more  than 2 or not 
if count == 2: #if count is bigger than 2 so it is not a prime number
    print("Value is Prime Number")
else:
    print("Vaue is not a Prime Number")
