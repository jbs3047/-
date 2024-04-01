from collections import deque
def bfs(x,y):
    q=deque()
    q.append((0,y,x,1))
    while q:
        boom,y,x,cnt=q.popleft()
        if x==m-1 and y==n-1:
            return cnt
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if lst[ny][nx]==1 and boom<1 and not vis[boom+1][ny][nx]:# 일단 깰 수 있으면 무조건 깨고 넘어감 (미방문시)
                    vis[boom+1][ny][nx]=1
                    q.append((boom+1,ny,nx,cnt+1))
                elif lst[ny][nx]==0 and not vis[boom][ny][nx]: #방문한 적 없음, 길 -> 일단 감
                    vis[boom][ny][nx]=1
                    q.append((boom,ny,nx,cnt+1))
    return -1

dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m=map(int,input().split())
lst=[list(map(int,input())) for _ in range(n)]
vis=[[[0]*(m) for _ in range(n)] for _ in range(2)]
ans=bfs(0,0)
print(ans)
