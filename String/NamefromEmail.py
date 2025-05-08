# this will find user id and domain name from email address
email = input('Entre Email Address -> ')
f = email.find('@') 
print('User ID: ', email[:f])
print('Domain Name:', email[f+1:]) 