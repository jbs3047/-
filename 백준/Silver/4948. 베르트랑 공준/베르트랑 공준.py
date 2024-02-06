lst=[True]*(123456*2+1)
m=int((123456*2)**0.5)
for i in range(2,m+1):
    if lst[i]==True:
        for j in range(2*i,123456*2+1,i):
            lst[j]=False

while True:
    n=int(input())
    cnt=0
    if n==0:
        break
    for i in range(n+1,2*n+1):
        if lst[i]==True:
            cnt+=1
    print(cnt)
