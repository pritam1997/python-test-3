n=int(input("ENter digit : "))
s=0
a=str(n)
for i in range(len(a)):
	q=int(a[i])
	s=s+q

print("Sum of digit is : {}".format(s))