#WAP to fiend greasted number
a=int(input("enter first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter third number : "))

if a==b and b==c and c==a:
 print("first,second and third is equl")
elif a>=b and a>=c:
 print("a first is gret")
elif b>=a and b>=c:
 print("b second is gret")
else:
 print("c third is gret")
