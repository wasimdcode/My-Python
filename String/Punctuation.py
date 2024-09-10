# It will Remove all of the Punctuation Marks 
s = input("Enter a String -> ")
punc = '''~!@#$%^&*()-[]{;}"':?<>|,./'''
s2 = ''
for x in s:
    if x not in punc:
        s2 += x
print(s2)