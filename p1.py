# WAP root of equaction
import math
a=float(input("Enter first no."))
b=float(input("Enter second no."))
c=float(input("Enter third no."))
d=b*b-4*a*c
if d<0:
 print("Roots are imaginary")
else:
 r1=(-b+math.sqrt(d))
 r2=(-b+math.sqrt(d))
 print("r1 ",r1)
 print("r2",r2)