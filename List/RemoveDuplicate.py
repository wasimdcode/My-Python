# it will any duplicate element in a list
list_ = [int(x) for x in input('Enter list numbers, separated by space -> ').split()]
list1 = []
for y in list_:
    if y not in list1: #it will check duplicate element
        list1.append(y)
print(list1)