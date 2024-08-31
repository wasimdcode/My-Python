# it will find factor of given number
n = int(input('Enter a Number '))
for i in range(1,n + 1):# this counter will check all the  numbers from 1 to "n"
    if n % i == 0: #this check "i" is divided by "n" or not
        print(i) #if it is true so it will print value
