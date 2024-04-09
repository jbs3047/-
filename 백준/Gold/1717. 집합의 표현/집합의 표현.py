def union(a,b):
    pa=findset(a)
    pb=findset(b)
    if pa==pb:
        return
    else:
        p[pb]=p[pa]
def findset(a):
    if a==p[a]:
        return a
    p[a]=findset(p[a])
    return p[a]
n,m=map(int,input().split())
p=[i for i in range(n+1)]
for _ in range(m):
    x,a,b=map(int,input().split())
    if x==0:
        union(a,b)
    else:
        if findset(a)==findset(b):
            print('YES')
        else:
            print("NO")