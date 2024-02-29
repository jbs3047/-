from collections import deque
dx=[0,1,0,-1]
dy=[-1,0,1,0]
def bfs():
    global shark,size,eat
    vis=[[0]*(n) for _ in range(n)]
    q=deque()
    x,y=shark
    q.append((x,y))
    vis[y][x]=1
    yammy=[]
    chk_y=n
    chk_t=n*n
    while q:
        x,y=q.popleft()
        if vis[y][x]>=chk_t:
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not vis[ny][nx]:
                #일단 먼저 지나가
                if lst[ny][nx]==0 or lst[ny][nx]==size:
                    vis[ny][nx]=vis[y][x]+1
                    q.append((nx,ny))
                #bfs돌리면 어짜피 거리 같은거끼리 나옴 -> y x 값 작은 순서로 어떻게? ->
                elif lst[ny][nx]<size:
                    vis[ny][nx]=vis[y][x]+1
                    if ny<=chk_y:#현재 최대 y값보다 작거나 같으면 x를 넣고 갱신
                        yammy.append(nx)
                        chk_y=ny
                        chk_t=vis[ny][nx]
    if not yammy:
        return -1
    chk_x=min(yammy)
    lst[chk_y][chk_x]=0
    eat+=1
    if eat==size:
        eat=0
        size+=1
    shark=[chk_x,chk_y]
    return vis[chk_y][chk_x]-1




n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
shark=[]
size=2
eat=0
for i in range(n):
    for j in range(n):
        if lst[i][j]==9:
            shark=[j,i]
            lst[i][j]=0

ans=0
while True:
    cnt=bfs()
    if cnt==-1:
        break
    ans+=cnt
print(ans)