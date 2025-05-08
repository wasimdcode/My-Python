#in will concate all the intergers in a list
L1 = [int(x) for x in input('Enter a string, Separatd by space_ -> ').split()]
s1 = ''
for i in L1:
    s1 += str(i)
print(int(s1))
