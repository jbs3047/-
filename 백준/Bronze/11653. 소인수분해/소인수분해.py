N = int(input())

lst = []

for num_1 in range(1, N + 1):
	if N % num_1 == 0:
		ans = []
		for num_2 in range(1, num_1 + 1):
			if num_1 % num_2 == 0:
				ans.append(num_2)
			
		if len(ans) == 2:
			lst.append(num_1)

for i in lst:
	while True:
		if N % i == 0:
			print(i)
			N /= i
		
		else:
			break
	
