#It will find minimum index of two values
f1 = ['Pizza','Nuggets','Hotdog','Noodles','Pasta','Burger']
f2 = ['Burger','Hotdog','Noodles','Pasta','Nuggets','Pizza']
index1 = 10
index2 = 10
for i in range(len(f1)):
    index = f2.index(f1[i])
    if i + index < index1 + index2:
        index1 = i
        index2 = index
print(f1[index1],index1+index2)
