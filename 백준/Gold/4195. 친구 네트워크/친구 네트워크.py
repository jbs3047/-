#4195 친구 네트워크
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def union(a,b):
    pa=findset(a)
    pb=findset(b)
    if pa!=pb:
        dic[pb]=pa
        cnt[pa]+=cnt[pb]
    return

def findset(a):
    if dic[a]==a:
        return a
    dic[a]=findset(dic[a])
    return dic[a]
t=int(input())
for tc in range(t):
    dic={}
    cnt={}
    f=int(input())
    for _ in range(f):
        x,y=map(str,input().split())
        if x not in dic:
            dic[x]=x
            cnt[x]=1
        if y not in dic:
            dic[y]=y
            cnt[y]=1
        union(x,y)
        print(cnt[findset(x)])

