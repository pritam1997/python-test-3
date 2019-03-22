n1 = int(input("Enter 1st no. :"))
n2 = int(input("Enter 1st no. :"))
n3 = int(input("Enter 1st no. :"))
s=0
if n1==n2 and n2==n3:
	s = 3*(n1+n2+n3)
	print(f"Thrice of the sum is {s}")
else:
	s = n1+n2+n3
	print(f"Sum is {s}")
