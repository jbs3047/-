a = [True] * (2500000 + 1)
m = int(2500000**0.5)
for i in range(2, m + 1):
    if a[i] == True:
        for j in range(i + i, 2500000 + 1, i):
            a[j] = False
                
a[0]=False
a[1]=False

n=int(input())
cnt=0
i=1
while True:
    if cnt==n:
        break
    else:
        i+=1
        if a[i]:
            cnt+=1
print(i)