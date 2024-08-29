# it will find sum of Negative(-) and Positive(+) Numbers Separately
sum_of_no = int(input("Enter Number of Number"))
p_sum = 0
n_sum = 0
count = 0
while count < sum_of_no:
    n = int(input("Enter Number "))
    count = count + 1
    if n > 0:
        p_sum = p_sum + n
    else:
        n_sum = n_sum + n
print("Sum of Positive Numbers", p_sum)
print("Sum of Negative Numbers", n_sum)

