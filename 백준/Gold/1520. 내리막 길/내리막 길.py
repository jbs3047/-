a,b=map(int,input().split())
lst=[]
for i in range(a):
    lst.append(list(map(int,input().split())))

dp=[[-1]*b for _ in range(a)]
dp[a-1][b-1]=1
def dfs(x,y):
    cnt=0
    if dp[y][x]!=-1:
        return dp[y][x]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<b and 0<=ny<a:
            if lst[ny][nx]<lst[y][x]:
                cnt+=dfs(nx,ny)
    dp[y][x]=cnt
    return dp[y][x]
print(dfs(0,0))

    