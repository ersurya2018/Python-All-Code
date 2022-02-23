class baseRectangle:
	def base(self,l,b):
		self.len=l
		self.bre=b
class rectangle(baseRectangle):
	def area(self):
		re=self.len*self.bre
		print("Area of rectangle : ",re)
		
obj=baseRectangle()
le=int(input("Enter the length : "))
br=int(input("Enter the bredth : "))
obj.base(le,br)
obj1=rectangle()
obj1.area()