import sys

N = int(input())
stack = []

for _ in range(N):
	prompt = sys.stdin.readline().split()
	
	if prompt[0] == 'push':
		stack.append(prompt[1])
	
	elif prompt[0] == 'pop':
		if stack:
			print(stack.pop())
		else:
			print(-1)
	
	elif prompt[0] == 'size':
		print(len(stack))

	elif prompt[0] == 'empty':
		if stack:
			print(0)
		else:
			print(1)
	
	elif prompt[0] == 'top':
		if stack:
			print(stack[-1])
		else:
			print(-1)