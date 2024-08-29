# it will Check Admin is Authorized or not
user_name = input('Enter User Name')
password = input('Enter Password')
if user_name == 'Law' and password == '1234' or user_name == 'Wasim' and password == '0000':
    print('Authorized')
else:
    print('Unauthorized')