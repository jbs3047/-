n=int(input())
dp=[-1 for _ in range(11)]
cnt=0
for i in range(n):
    x,y=map(int,input().split())
    if dp[x]==-1:
        dp[x]=y
    elif dp[x]!=y:
        dp[x]=y
        cnt+=1
print(cnt)
