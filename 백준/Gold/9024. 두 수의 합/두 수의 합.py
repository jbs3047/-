t=int(input())
for tc in range(t):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    lst.sort()
    start=0
    end=n-1
    cnt=0
    mx=5*(10**8)+1
    while start<end:
        sm=lst[start]+lst[end]
        if sm>k:
            end-=1
            if abs(sm-k)<mx:
                mx=abs(sm-k)
                cnt=1
            elif abs(sm-k)==mx:
                cnt+=1
        elif sm<k:
            start+=1
            if abs(sm-k)<mx:
                mx=abs(sm-k)
                cnt=1
            elif abs(sm-k)==mx:
                cnt+=1
        else:
            if abs(sm-k)<mx:
                mx=abs(sm-k)
                cnt=1
            else:
                cnt+=1
            start+=1
    print(cnt)
