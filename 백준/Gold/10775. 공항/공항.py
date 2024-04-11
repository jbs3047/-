#10775 공항
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def union(a,b):
    pa=findset(a)
    pb=findset(b)
    p[pa]=pb

def findset(a):
    if p[a]==a:
        return a
    p[a]=findset(p[a])
    return p[a]
n=int(input())
p=[i for i in range(n+1)]
x=int(input())
cnt=0
for i in range(x):
    chk=int(input())
    port=findset(chk)
    if port:
        cnt+=1
        union(port,port-1)
    else:
        break
print(cnt)