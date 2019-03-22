filename = input("Enter filename : ")

n=len(filename)
for i in range(n):
	if filename[i]=='.':
		get=i
for i in range(get+1,n):
	print(filename[i],end="")