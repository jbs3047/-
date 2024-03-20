def bag(lst,x,cnt):
    if x>c:
        return
    if cnt==len(lst):
        ans1.append(x)
        return
    bag(lst,x+lst[cnt],cnt+1)
    bag(lst,x,cnt+1)
def bag2(lst,x,cnt):
    if x>c:
        return
    if cnt==len(lst):
        ans2.append(x)
        return
    bag2(lst,x+lst[cnt],cnt+1)
    bag2(lst,x,cnt+1)
def upperbound(lst,target):
    start=0
    end=len(lst)-1
    while start<=end:
        mid=(start+end)//2
        if target>=lst[mid]:
            start=mid+1
        else:
            end=mid-1
    return end+1


n,c=map(int,input().split())
lst=list(map(int,input().split()))
lst1=lst[:n//2]
lst2=lst[n//2:]
ans1=[]
ans2=[]
bag(lst1,0,0)
bag2(lst2,0,0)
ans2.sort()
cnt=0
for i in range(len(ans1)):
    x=ans1[i]
    cnt+=upperbound(ans2,c-x)
print(cnt)