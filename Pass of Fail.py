#it Check 3 subjects marks if student is pass in all three sujects then it give pass otherwise Fail
E = int(input('Enter English Marks'))
M = int(input('Enter Math Marks'))
S = int(input('Enter Science Marks'))
if E >= 35 and M >= 35 and S >= 35:
    print('Passed')
else:
    print('Failed')