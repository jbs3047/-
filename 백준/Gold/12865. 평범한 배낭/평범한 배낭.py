n,m=map(int,input().split())
bag=[(0,0)]
for i in range(n):
    w,v=map(int,input().split())
    bag.append((w,v))

dp=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):#물건 개수
    w,v=bag[i]
    for x in range(1,m+1):#무게
        if x-w<0:
            dp[i][x]=dp[i-1][x]
        else:
            dp[i][x]=max(dp[i-1][x],dp[i-1][x-w]+v)
print(max(dp[n]))
    