import sys
sys.setrecursionlimit(10**5)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m=map(int,input().split())

lst=[list(map(str,input())) for _ in range(n)]
vis=[[0]*m for _ in range(n)]
end=[[0]*m for _ in range(n)]
lineup=[]
ans=0
def dfs(x,y):
    global ans
    for i in range(4):
        num=int(lst[y][x])
        nx=x+num*dx[i]
        ny=y+num*dy[i]
        if 0<=nx<m and 0<=ny<n and lst[ny][nx]!="H":
            if vis[ny][nx]:
                ans=-1
                return
            if end[ny][nx]:
                continue
            vis[ny][nx]=1
            dfs(nx,ny)
            vis[ny][nx]=0
    end[y][x]=1
    lineup.append([x,y])

dfs(0,0)
if ans==-1:
    print(-1)
else:
    dp=[[1]*m for _ in range(n)]
    while lineup:
        x,y=lineup.pop()
        for i in range(4):
            num=int(lst[y][x])
            nx=x+num*dx[i]
            ny=y+num*dy[i]
            if 0<=nx<m and 0<=ny<n and lst[ny][nx]!="H":
                dp[ny][nx]=max(dp[ny][nx],dp[y][x]+1)
    for i in range(n):
        for j in range(m):
            ans=max(ans,dp[i][j])
    print(ans)