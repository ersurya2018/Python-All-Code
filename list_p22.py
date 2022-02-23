#list example in different built in method
x=[10,20,30,40,50]
print("the list print before not doing operation")
print(x)

print("the list print after len operation")
print(len(x))    #fiend the length of list 
x.append(3)	# add new data in ending point
print("the list print after append operation")
print(x)
x.insert(0,70)	#new element at given position
print("the list print after insert operation")
print(x)
y=['sd','df','fg']
x.extend(y)
print("the list print after extend operation")
print(len(x))
print(x)