import heapq
t=int(input())
for tc in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    heapq.heapify(lst)
    cnt=0
    while len(lst)>1:
        x=heapq.heappop(lst)
        y=heapq.heappop(lst)
        cnt+=x+y
        heapq.heappush(lst,x+y)
    print(cnt)