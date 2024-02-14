T = int(input())

for _ in range(T):
	string = input()
	stack = []

	for i in string:
		if i == '(':
			stack.append(i)

		else:
			if stack:
				stack.pop()
			else:
				result = 'NO'
				break
	
	else:
		result = 'YES'
	
	if stack:
		result = 'NO'

	print(result)