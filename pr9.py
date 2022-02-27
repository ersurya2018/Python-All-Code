def a(s):
    return s[::-1]
def b(s):
    rev=a(s)
    if s==rev:
        return True
    else:
        return False
str=input("Enter the string for chaking palindrome or not : ")
print (str)
ans=b(str)
if ans==1:
    print("This is palindrome ")
else:
    print("This is not palindrome ")
