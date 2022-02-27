#WAP to find factorical of given number
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

x=int(input("Enter the number find factorical : "))
print(fact(x))
