def division(b,c):
 return(b/c)
def fact(b):
 if(b==1 or b==0):
  return 1
 else:
  i=1
 #fact=1
  while(i<=10):
   fact=b*(b+1)
   i=i+1
   return fact
 
x=int(input("first number"))
y=int(input("second number"))
#e=division(x/y)
f=fact(x)
#print("divi : ",e)
print("fact : ",f)