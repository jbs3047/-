n=int(input())
lst=list(map(int,input().split()))
lst.sort()
prefix=[0 for _ in range(len(lst))]
prefix[0]=lst[0]
for i in range(1,len(lst)):
    prefix[i]=prefix[i-1]+lst[i]
ans=[0,prefix[0]]
if prefix[0]!=1:
    print(1)
else:
    answer=0
    chk=0
    for i in range(1,n):
        now=ans
        new=[lst[i],prefix[i]]
        if ans[1]+1>=new[0]:
            ans=[0,prefix[i]]
        else:
            answer=now[1]+1
            chk=1
            break
    if chk:
        print(answer)
    else:
        print(prefix[-1]+1)