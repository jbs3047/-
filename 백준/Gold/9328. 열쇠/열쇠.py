from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs():
    ans=0
    vis=[[0]*(w+2) for _ in range(h+2)]
    q=deque()
    q.append((0,0))
    vis[0][0]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<w+2 and 0<=ny<h+2 and lst[ny][nx]!='*' and not vis[ny][nx]:
                if lst[ny][nx]=='.':
                    vis[ny][nx]=1
                    q.append((nx,ny))
                elif lst[ny][nx]=='$':
                    ans+=1
                    vis[ny][nx]=1
                    lst[ny][nx]='.'
                    q.append((nx,ny))
                else:
                    if lst[ny][nx].isupper(): # 문
                        if door[ord(lst[ny][nx])-65]:
                            lst[ny][nx]='.'
                            vis[ny][nx]=1
                            q.append((nx,ny))
                    else: # 열쇠 -> 열쇠 먹으면 vis랑 큐 초기화 후 다시 돌기
                        door[ord(lst[ny][nx])-97]=1
                        lst[ny][nx]='.'
                        vis=[[0]*(w+2) for _ in range(h+2)]
                        vis[ny][nx]=1
                        q=deque()
                        q.append((nx,ny))
    return ans


t=int(input())
for tc in range(t):
    h,w=map(int,input().split())
    lst=[]
    lst.append(['.']*(w+2))
    for _ in range(h):
        lst.append(['.']+list(map(str,input()))+['.'])
    lst.append(['.']*(w+2))
    door=[0 for _ in range(26)]
    keys=str(input())
    for key in keys:
        if key=='0':
            break
        door[ord(key)-97]=1
    for i in range(1,h+1):
        for j in range(1,w+1):
            if lst[i][j].isupper() and door[ord(lst[i][j])-65]:
                lst[i][j]='.'
    print(bfs())