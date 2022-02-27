
num = int(input("Enter a number : "))
from time import sleep
i=1;
while i<=10:
    res=i*num
    sleep(1)
    print(num," * ",i," = ",res)
    i=i+1
