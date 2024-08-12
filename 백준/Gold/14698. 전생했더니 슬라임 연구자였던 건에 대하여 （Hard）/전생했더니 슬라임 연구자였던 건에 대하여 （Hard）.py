# 14698 전생했더니 슬라임 연구자였던 건에 대하여(Hard)
import sys
import heapq
input=sys.stdin.readline
t = int(input())
for tc in range(t):
    n = int(input())
    lst=list(map(int, input().split()))
    heap =[]
    for i in lst:
        heapq.heappush(heap,i)
    ans = 1
    while len(heap) >= 2:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        heapq.heappush(heap, x * y)
        ans *= (x * y)%1000000007
    print(ans % 1000000007)
