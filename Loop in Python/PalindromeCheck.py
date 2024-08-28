# it will Reverse Number sequence
n = int(input("Enter a Number"))
m = n
rev = 0
while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r

if m == rev:
    print("it is a Palindrom")
else:
    print("it is Not Palindrome")
