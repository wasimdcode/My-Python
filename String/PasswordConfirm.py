# it will confirm Password it is same or not 
pass1 = input('Enter a Password -> ')
Cpass = input('Enter Confirm Passwrod -> ')
if pass1 == Cpass:
    print('Password Confirmend')
elif pass1.casefold() == Cpass.casefold(): #it will Check Cases
    print('Try again ! Please Check the Cases of password ')
else:
    print('No ! They are not Matching Try them again ')
