#it will count salary based on weekly work hours 
work_h = [int(x) for x in input('Enter hours per.day in entire week, separeted by space -> ').split()]
wage = int(input('Enter Wage per hour -> '))
h = 0 #total = sum(work_h) it will give the  sum of list
for x in work_h:
    h = h + x 
    salary = h * wage
print('Salary is ', salary)