dp=[[0,0,0] for _ in range(1516)]
dp[1][1]=1
dp[1][2]=1
for i in range(2,1516):
    dp[i][0]=dp[i-1][1]+dp[i-1][2]
    dp[i][1]=dp[i-1][0]+dp[i-1][2]
    dp[i][2]=dp[i-1][0]+dp[i-1][2]

n=int(input())
print(dp[n-1][1]%1000000007)