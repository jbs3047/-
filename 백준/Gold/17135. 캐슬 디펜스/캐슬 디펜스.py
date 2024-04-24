from itertools import combinations
from collections import deque
dx=[-1,0,1]
dy=[0,-1,0]


def shoot(archor):
    arr=[item[:] for item in lst]
    die=[[0]*m for _ in range(n)]
    cnt=0
    for i in range(n-1,-1,-1): # 적 죽이는거랑 내려오는거 따로 구현하는게 복잡함 -> 궁수가 한칸씩 올라가는 느낌으로 접근
        now=[]
        for xx in archor:
            q=deque()
            q.append([i,xx,1]) # 궁수 바로 윗칸 , 거리 1
            while q:
                y,x,dis=q.popleft()
                if arr[y][x]==1: # 적 만남 -> 어짜피 탐색 순서가 왼 위 오른쪽이므로 제일 먼저 만나는게 타겟
                    now.append((y,x))
                    if die[y][x]==0:
                        die[y][x]=1
                        cnt+=1
                    break
                if dis<d:
                    for j in range(3):
                        nx=x+dx[j]
                        ny=y+dy[j]
                        if 0<=nx<m and 0<=ny<n:
                            q.append((ny,nx,dis+1))
        for y,x in now:
            arr[y][x]=0
    return cnt


n,m,d=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
enemy=[]
ans=0
for k in combinations([i for i in range(m)],3):
    ans=max(ans,shoot(k))
print(ans)
