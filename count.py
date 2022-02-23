#12345-------5
num=int(input("Enter the number : "))
c=0
while num>0:
 c=c+1
 num=int(num/10)
print("total digit : ",c)