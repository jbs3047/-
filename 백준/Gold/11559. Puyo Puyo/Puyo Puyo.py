from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(y,x,color):
    global chk
    q=deque()
    q.append((y,x))
    boom=[]
    boom.append([y,x])
    while q:
        y,x=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<6 and 0<=ny<12 and not vis[ny][nx]:
                if lst[ny][nx]==color:
                    vis[ny][nx]=1
                    q.append((ny,nx))
                    boom.append([ny,nx])
    if len(boom)>=4:
        for y,x in boom:
            lst[y][x]='.'
        chk=1


def drop():
    for j in range(6):
        cnt=11
        for i in range(11,-1,-1):
            if lst[i][j]!='.':
                x=lst[i][j]
                lst[i][j]='.'
                lst[cnt][j]=x
                cnt-=1


lst=[list(map(str,input())) for _ in range(12)]
cnt=0
while True:
    chk=0
    vis=[[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if lst[i][j]=='.':
                continue
            vis[i][j]=1
            bfs(i,j,lst[i][j])
    drop()
    if chk:
        cnt+=1
    else:
        break
print(cnt)