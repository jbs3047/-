n=int(input())
lst=list(map(int,input().split()))
lst.sort()
cnt=0
for i in range(n):
    x=lst[i]
    start=0
    end=n-1
    while start<end:
        sm=lst[start]+lst[end]
        if sm==x:
            if start!=i and end!=i:
                cnt+=1
                break
            elif start!=i and end==i:
                end-=1
                if lst[start]+lst[end]==x and end!=i and start<end:
                    cnt+=1
                    break
            else:
                start+=1
                if lst[start]+lst[end]==x and start!=i and start<end:
                    cnt+=1
                    break
        sm=lst[start]+lst[end]
        if sm>x:
            end-=1
        else:
            start+=1
print(cnt)