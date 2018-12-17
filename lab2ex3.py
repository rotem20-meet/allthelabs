a=[12,23,34,45]
b=[12,111,223,23]
c=[]
for i in a:
    for t in b: 
        if i==t:
            c.append(i)

print(c)
