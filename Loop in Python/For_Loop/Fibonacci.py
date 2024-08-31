# it will show fibonacci terms 
n = int(input("Enter How many terms you want to print "))
a = 0
b = 1
for t in range(n): #calculation should look like this a + b, c = a + b
    print(a) 
    c = a + b #ex :- a=0, b=1, 1 = 0 + 1
    a = b # b = 1 so a = 1
    b = c # c = 1 so b = 1
    