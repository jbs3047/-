n=int(input())
lst=list(map(int,input().split()))
mx=max(lst)
score=[100001]*1000001
for i in lst:
    score[i]=0
for i in range(1,mx+1):
    if score[i]!=100001:
        for j in range(2*i,mx+1,i):
            if score[j]!=100001:
                score[i]+=1
                score[j]-=1
for i in lst:
    print(score[i],end=' ')