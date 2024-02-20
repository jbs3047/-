n=int(input())
dp=[0 for _ in range(1001)]
dp[1]=1
dp[2]=5
dp[3]=11
dp[4]=36
for i in range(5,n+1):
    dp[i]=(dp[i-1]+5*dp[i-2]+dp[i-3]-dp[i-4])%1000
print(dp[n]%1000)