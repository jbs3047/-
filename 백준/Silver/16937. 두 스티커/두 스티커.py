h,w=map(int,input().split())
n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        x1,y1=lst[i]
        x2,y2=lst[j]
        if (x1+x2<=h and max(y1,y2)<=w) or (y1+y2<=w and max(x1,x2)<=h):
            ans=max(ans,(x1*y1+x2*y2))
        if (y1+x2<=h and max(x1,y2)<=w) or (x1+y2<=w and max(y1,x2)<=h):
            ans=max(ans,(x1*y1+x2*y2))
        if (x1+y2<=h and max(y1,x2)<=w) or (y1+x2<=w and max(x1,y2)<=h):
            ans=max(ans,(x1*y1+x2*y2))
        if (y1+y2<=h and max(x1,x2)<=w) or (x1+x2<=w and max(y1,y2)<=h):
            ans=max(ans,(x1*y1+x2*y2))
print(ans)