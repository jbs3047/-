n=int(input())
k=int(input())
start=1
end=k
ans=0
while start<=end:
    cnt=0
    mid=(start+end)//2
    for i in range(1,n+1): #i열 -> i*j
        cnt+=min(mid//i,n) # mid//i가 n보다 클 경우 대비
    if cnt>=k:
        end=mid-1
        ans=mid
    else:
        start=mid+1
print(ans)
