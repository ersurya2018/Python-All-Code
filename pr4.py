#fourth
num=int(input("What is your favorite number ?: "))
if num>1:
    for i in range(2,num):                  #for loop
        if num%i==0:                        # if Steatement
            print(num,"is not prime")
            print(i,"time",num//i,"is",num)
            break                           #break keyword
    else:                                   # else Statement
        print(num,"is prime")
else:
    print(num,"is not prime")