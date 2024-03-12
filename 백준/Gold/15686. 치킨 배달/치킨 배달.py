from itertools import combinations
n,m=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
house=[]
chicken=[]
ans=10000000
for i in range(n):
    for j in range(n):
        if lst[i][j]==1:
            house.append([j,i])
        elif lst[i][j]==2:
            chicken.append([j,i])
for i in combinations(chicken,m):
    mn=0
    for j in house:
        chk=101
        for k in range(m):
            chk=min(chk,abs(i[k][0]-j[0])+abs(i[k][1]-j[1]))
        mn+=chk
    ans=min(ans,mn)
print(ans)