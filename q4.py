n=int(input("Enter no. : "))

print("Your no. is greater than 17")
if n > 17:
	r = n-17
	r=r+r
	print(f"Double the absolute difference is : {r}")
else:
	print("Your no. is less than 17")
