#1043 거짓말
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def union(a,b):
    pa=findset(a)
    pb=findset(b)
    if a!=b:
        if pb>pa:
            p[pb]=pa
        else:
            p[pa]=pb
    else:
        return

def findset(a):
    if p[a]==a:
        return a
    p[a]=findset(p[a])
    return p[a]
n,m=map(int,input().split())
p=[i for i in range(n+1)]
result=0
lie=list(map(int,input().split()))
if lie[0]==0:
    print(m)
else:
    for i in range(1,len(lie)):
        union(0,lie[i])
    lst=[list(map(int,input().split())) for _ in range(m)]
    for i in lst:
        if i[0]!=1:
            for j in range(1,len(i)-1):
                union(i[j],i[j+1])
    for i in lst:
        chk=0
        for j in i[1:]:
            if findset(j):
                chk+=1
        if chk==len(i)-1:
            result+=1
    print(result)