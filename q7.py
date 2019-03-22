v=['a','i','o','u','e']

s=input("Enter string to check you pass vowels or not : ")
c=0
for i in s:
	if i in v:
		c+=1
if c>0:
	print("you passed vowels in string")
else:
	print("YOu not passed vowels")
