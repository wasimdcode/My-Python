# It check String is Palindrome or not  ex. madam reversed "madam"
n = input("Enter a String -> ")
if n == n[::-1]:
    print("Yess it is a Palindrome", n[::-1])
else:
    print("No ! it is not a Palindrome","Converted", n + n[::-1])
