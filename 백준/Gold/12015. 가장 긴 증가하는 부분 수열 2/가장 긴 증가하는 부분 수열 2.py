def lower(lst,target):
    start=0
    end=len(lst)-1
    while start<end:
        mid=(start+end)//2
        if target>lst[mid]:
            start=mid+1
        else:
            end=mid
    return end

n=int(input())
lst=list(map(int,input().split()))
M=[-1]
parent=[]
for i in lst:
    if M[-1]<i:
        M.append(i)
    else:
        M[lower(M,i)]=i
print(len(M)-1)

