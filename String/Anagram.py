# it will check string is anagram or not 
a1 = input('Enter frist Word -> ')
a2 = input('Enter Second Word -> ')
if len(a1) != len(a2): 
    print("No  ! Not a Anagram")
else:
    for x in a1:
        if x not in a2:
            print("No ! Not a Anagram")
            break;
    else:
        print("Yess ! Anagram")
