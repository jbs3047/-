from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m=map(int,input().split())#세로 가로
lst=[list(map(int,input())) for _ in range(n)]
#시작점 끝점 bfs 돌린 후 모든 벽에서 탐색 돌려서 좌우에 있으면 최소합
lst2=[i[:] for i in lst]#시작점
lst3=[i[:] for i in lst]#끝점
def bfs(x,y,map):
    q=deque()
    q.append((x,y))
    map[y][x]=2
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if map[ny][nx]==0:
                    map[ny][nx]=map[y][x]+1
                    q.append((nx,ny))
def check(x,y):
    chk1=n*m+2
    chk2=n*m+2
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and lst2[ny][nx]!=0 and lst2[ny][nx]!=1:
            chk1=min(chk1,lst2[ny][nx])
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and lst3[ny][nx]!=0 and lst3[ny][nx]!=1:
            chk2=min(chk2,lst3[ny][nx])
    #print(x,y)
    #print(chk1,chk2)
    #print('-----')
    if chk1!=n*m+2 and chk2!=n*m+2:
        return chk1+chk2-1
    return n*m+2

bfs(0,0,lst2)
#print(lst2)
bfs(m-1,n-1,lst3)
#print(lst3)
if lst3[0][0]!=0:
    ans=lst3[0][0]-1
else:
    ans=n*m+2
for i in range(n):
    for j in range(m):
        if lst[i][j]==1:
            ans=min(ans,check(j,i))
if ans==n*m+2:
    print(-1)
else:
    print(ans)

