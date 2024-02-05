n,z=map(int,input().split())
lst=[]
while n>=z:
	if n%z>9:
		lst.append(chr(n%z+55))
	else:
		lst.append(n%z)
	n//=z
if n>9:
	lst.append(chr(n+55))
else:
	lst.append(n)
lst.reverse()
for i in lst:
	print(i,end='')