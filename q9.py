ch=str(input("CHoose no. you want enter in feet for \"ft\" and inches for \"in\" : "))

if ch == "ft":
	c=30.48
	n=int(input("Enter height(in feet) to convert centimeters : "))
	f=c*n 
	print(f"{f} centimeters")

elif ch == "in":
	c=2.54
	n=int(input("Enter height(in inches) to convert centimeters : "))
	i=c*n	
	print(f"{i} centimeters")
