import sys
import heapq
input=sys.stdin.readline
n,k=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
bag=[int(input()) for _ in range(k)]

bag.sort()
lst.sort()
ans=0
use=[]
for i in bag:
    while lst and lst[0][0]<=i:
        heapq.heappush(use,-lst[0][1])
        heapq.heappop(lst)
    if use:
        ans-=heapq.heappop(use)
print(ans)