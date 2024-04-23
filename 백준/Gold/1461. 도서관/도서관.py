# from itertools import combinations
#
# n,m,d=map(int,input().split())
# lst=[list(map(int,input().split())) for _ in range(n)]+[[0]*m]
# enemy=[]
# for i in range(n):
#     for j in range(m):
#         if lst[i][j]:
#             enemy.append([j,i])
# for i in combinations([i for i in range(m)],3):
#     archer=[]
#     for j in i:
#         archer.append([j,n])

n,m=map(int,input().split())
lst=list(map(int,input().split()))
pos=[]
neg=[]
for i in lst:
    if i<0:
        neg.append(-i)
    else:
        pos.append(i)
neg.sort()
pos.sort()
cnt=[]
x=len(neg)-1
y=len(pos)-1
while True:
    if x-m+1>=0:
        cnt.append(neg[x])
        x-=m
    else:
        if x<0:
            break
        cnt.append(neg[x])
        break
while True:
    if y-m+1>=0:
        cnt.append(pos[y])
        y-=m
    else:
        if y<0:
            break
        cnt.append(pos[y])
        break

ans=0
for i in cnt:
    ans+=i*2
ans-=max(cnt)
print(ans)