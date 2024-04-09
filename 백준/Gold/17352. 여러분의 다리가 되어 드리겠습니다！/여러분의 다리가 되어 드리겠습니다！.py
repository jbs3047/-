def union(a,b):
    pa=findset(a)
    pb=findset(b)
    if pa==pb:
        return
    p[pb]=pa

def findset(a):
    if p[a]!=a:
        p[a]=findset(p[a])
    return p[a]
n=int(input())
p=[i for i in range(n+1)]
for _ in range(n-2):
    a,b=map(int,input().split())
    union(a,b)
for i in range(1,n+1):
    if i==p[i]:
        print(i,end=' ')