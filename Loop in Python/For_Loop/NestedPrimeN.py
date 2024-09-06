#it will print prime numbers from 1 ot 100 with neseted loop
for n in range(1,100+1):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n)
            