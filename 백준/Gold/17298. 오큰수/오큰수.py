n=int(input())
lst=list(map(int,input().split()))
stack=[]
ans=[0 for _ in range(n)]
for i in range(n-1,-1,-1):
    now=lst[i]
    while stack and now>=stack[-1]:
        stack.pop()
    if not stack:
        ans[i]=-1
    else:
        ans[i]=stack[-1]
    stack.append(now)
print(*ans)