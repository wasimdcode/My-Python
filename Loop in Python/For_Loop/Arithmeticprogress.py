# it will print Arithmetic Progression of given number
a = int(input('Enter Intital term '))
d = int(input('Enter Difference between terms '))
n = int(input('Enter How many terms You want to Print ?'))
for t in range(a,a + n * d, d):
    print(t)