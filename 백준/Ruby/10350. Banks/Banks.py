import math
n=int(input())
lst=list(map(int,input().split()))
presum=[0 for _ in range(2*n+1)]
cnt=0
sm=sum(lst)
for i in range(1,2*n+1):
    presum[i]=presum[i-1]+lst[(i-1)%n]
for i in range(1,n):
    for j in range(n):
        ans=presum[i+j]-presum[j]
        if ans<0:
            cnt+=math.ceil(abs(ans)/sm)
print(cnt)
