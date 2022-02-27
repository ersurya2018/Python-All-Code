# WAP to print fibonacci sequence up to n term
n=int(input("How many terms you want in fibonacci sequence ? "))
n1=0 # First term
n2=1# Second term
print("Fibonacci Sequence : ")
print(n1,n2,end=" ")
i=1
while(i<=n-2):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3
    i=i+1