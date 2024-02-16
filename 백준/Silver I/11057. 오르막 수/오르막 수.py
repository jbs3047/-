n=int(input())
dp=[[0]*10 for _ in range(1001)]
dp[1]=[1,1,1,1,1,1,1,1,1,1]
dp[2]=[1,2,3,4,5,6,7,8,9,10]#n으로 끝나는 가짓수
for i in range(3,n+1):
    for j in range(10):
        dp[i][j]=(sum(dp[i-1][:j+1]))%10007
print(sum(dp[n])%10007)