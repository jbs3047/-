import copy
from collections import deque
r,c=map(int,input().split())
lst=[list(map(str,input())) for _ in range(r)]#비버
lst2=copy.deepcopy(lst)#물
lst3=[[0]*c for _ in range(r)]
water=[]
chk=0
size=2
for i in range(r):
    for j in range(c):
        if lst[i][j]=="D":
            lst[i][j]=0
            lst2[i][j]=-1
            escape=[j,i]
        elif lst[i][j]=="S":
            beaverx=j
            beavery=i
            lst2[i][j]=0
        elif lst[i][j]=="*":
            lst[i][j]=0
            lst2[i][j]=0
            water.append((j,i))
        elif lst[i][j]==".":
            lst[i][j]=0
            lst2[i][j]=0
        else:
            lst2[i][j]=-1

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def beaver_run(x,y):
    q=deque()
    q.append((x,y))
    lst[y][x]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<c and 0<=ny<r:
                if lst[ny][nx]==0:
                    lst[ny][nx]=lst[y][x]+1
                    q.append((nx,ny))
def water_run(x,y):
    q=deque()
    q.append((x,y))
    lst2[y][x]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<c and 0<=ny<r:
                if lst2[ny][nx]==0 or lst2[ny][nx]>lst2[y][x]+1:
                    lst2[ny][nx]=lst2[y][x]+1
                    q.append((nx,ny))
def bfs(x,y):
    q=deque()
    q.append((x,y))
    lst3[y][x]=2
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<c and 0<=ny<r:
                if lst3[ny][nx]==1:
                    lst3[ny][nx]=lst3[y][x]+1
                    q.append((nx,ny))
#print(lst)
#print(beaverx,beavery)
#print(lst2)
#print(water)
beaver_run(beaverx,beavery)
for x,y in water:
    water_run(x,y)
#print(lst)
#print(lst2)
for y in range(r):
    for x in range(c):
        if lst[y][x]!=0 and lst2[y][x]==0:
            lst3[y][x]=1
        elif lst[y][x]!="X" and lst2[y][x]!="X" and lst[y][x]<lst2[y][x]:
            lst3[y][x]=1
lst3[escape[1]][escape[0]]=1
#print(lst3)
bfs(beaverx,beavery)
#print(lst3)
ans=lst3[escape[1]][escape[0]]
if ans==1:
    print("KAKTUS")
else:
    print(ans-2)