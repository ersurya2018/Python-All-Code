# five
a=[]
for x in range(2000,2500):
    if x%17==00 and x%5!=0:
        a.append(str(x))
print(' '.join(a))