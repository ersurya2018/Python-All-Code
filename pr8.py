def revs(s):
    str=""
    for i in s:
        str=i+str
    return str
s=input("Enter the string : ")
print("Orginal string is : ",end="")
print (s)

print("reverse string : ",end="")
print(revs(s))