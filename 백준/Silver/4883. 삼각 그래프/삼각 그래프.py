cnt=1
while True:
    n=int(input())
    if n==0:
        break
    lst=[list(map(int,input().split())) for _ in range(n)]
    dp=[[0]*3 for _ in range(n)]
    dp[0]=[10000,lst[0][1],lst[0][1]+lst[0][2]]
    for i in range(1,n):
        dp[i][0]=min(dp[i-1][0],dp[i-1][1])+lst[i][0]
        dp[i][1]=min(dp[i][0],dp[i-1][0],dp[i-1][1],dp[i-1][2])+lst[i][1]
        dp[i][2]=min(dp[i][1],dp[i-1][1],dp[i-1][2])+lst[i][2]

    print(f'{cnt}. {dp[n-1][1]}') 
    cnt+=1

