# This will Display Credit Card number in "**** **** **** 8374" Format
card_no = input('Enter 16 Digits Card Number -> ')
if len(card_no) == 16: #it will check digits 16 
    last_4 = card_no[12::] #it will give last digits
    display = '**** ' + '**** ' + '**** ' + last_4   #it will add "* " before last digits
    print(display)
else:
    print('Please ! Enter 16 Digits Number ')
#Diffirent approach by sir
'''card_no = input('Enter Card Number ')
lastdigits = card_no[12::]
four = '*' * 4 + ' '
displayno = four * 3 + lastdigits
print(displayno)'''

