# input ten number in the list user help
mylist=[]
print("Enter the ten number")
for i in range(0,10):
 n=int(input())
 mylist.append(n)
print(mylist)
print("max no = ",max(mylist))
print("min no = ",min(mylist))