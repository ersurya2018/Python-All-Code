b=[]
c=[]
d=[]
e=[]

for i in range(0,3):
 n=int(input("Enter first number :"))
 m=int(input("Enter second number :"))
 sum=n+m
 sub=m-n
 multi=n*m
 divi=m/n
 b.append(sum)
 c.append(sub)
 d.append(multi)
 e.append(divi)
print("som  & totel list is",b)
print("sub  & totel list is",c)
print("multi  & totel list is",d)
print("divi & totel list is",e)