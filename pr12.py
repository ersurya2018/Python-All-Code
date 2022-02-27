def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divi(a,b):
    return a/b
def modu(a,b):
    return a%b

print("Please select option-\n"
 "1. add\n"
 "2. subtraction\n"
 "3. multiply \n"
 "4. divison \n"
 "5. modulas\n")

select=int(input("Enter operations from 1,2,3,4,5\n"))
if select<6:
    num1=int(input("Enter the first number : "))
    num2=int(input("Enter the second number : "))
    if select==1:
        print(num1," + ",num2," = ",add(num1,num2))
    elif select==2:
        print(num1," - ",num2," = ",
            sub(num1,num2))
    elif select==3:
        print(num1," * ",num2," = ",
            multi(num1,num2))
    elif select==4:
        print(num1," / ",num2," = ",
            divi(num1,num2))
    elif select==5:
        print(num1," % ",num2," = ",
            modu(num1,num2))
else:
    print("Please input valid number becase this is a invalid number ")
    