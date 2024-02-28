import sys
input=sys.stdin.readline
a=int(input())
lst=[[0]*(a+1)]
for _ in range(a):
    b=[0]+list(map(int,input().split()))
    lst.append(b)
dp=[[[0,0,0] for _ in range(a+1)] for _ in range(a+1)] # 가로 세로 대각
dp[1][2][0]=1
for y in range(1,a+1):
    for x in range(3,a+1):
        if lst[y][x]==0:
            pass
            dp[y][x][0]=dp[y][x-1][0]+dp[y][x-1][2]
            dp[y][x][1]=dp[y-1][x][1]+dp[y-1][x][2]
            if lst[y-1][x]==1 or lst[y][x-1]==1:
                dp[y][x][2]=0
            else:
                dp[y][x][2]=dp[y-1][x-1][0]+dp[y-1][x-1][1]+dp[y-1][x-1][2]
        else:
            dp[y][x]=[0,0,0]
print(sum(dp[y][x]))