from collections import deque
n=int(input())
lst=list(map(int,input().split()))
ans=[i for i in range(1,n+1)]
lst.reverse()
q=deque()
for i in range(n):
    if lst[i]==1:
        q.appendleft(ans[i])
    elif lst[i]==2:
        x=q.popleft()
        q.appendleft(ans[i])
        q.appendleft(x)
    else:
        q.append(ans[i])

print(*q)
