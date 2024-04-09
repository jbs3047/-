import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def union(a,b):
    a=findset(a)
    b=findset(b)
    if a!=b:
        p[b]=a

def findset(a):
    if p[a]==a:
        return a
    p[a]=findset(p[a])
    return p[a]
n,m=map(int,input().split())
p=[i for i in range(n)]
result=0
for i in range(m):
    a,b=map(int,input().split())
    if findset(a)!=findset(b):
        union(a,b)
    else:
        result=i+1
        break
print(result)