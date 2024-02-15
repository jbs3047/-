n=int(input())

dp=[0 for _ in range(1001)]
dp[2]=3
dp[4]=11
for i in range(6,n+1,2):
    dp[i]=(4*dp[i-2]-dp[i-4])%1000000007

print(dp[n])