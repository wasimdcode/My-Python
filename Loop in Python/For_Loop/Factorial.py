# Factorial is 5 = 1*2*3*4*5=120 this program will give Factorial number
n = int(input('Enter a Number '))
fact = 1 
for count in range(1,n+1): #this will start form 1 end at n+1 it stop at "n"
    fact = fact * count #it will multiply each number until "n"
    
print("Facotrial of",n,"is",fact)