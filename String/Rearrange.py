# This Will Rearrange A string Lowercase to Uppercase
s = input("Enter a String")
lower = ''
upper = ''
for x in s:
    if x.islower():
        lower += x
    else:
        upper += x
s2 = lower + upper
print(s2)
    