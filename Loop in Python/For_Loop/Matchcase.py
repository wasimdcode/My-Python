# this is the example of match case 
day = int(input("Enter Day Number"))
#this will print Day by number
match day:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case _:
        print('Holiday')

