n=int(input())
lst=list(map(int,input().split()))+[0,0]
cnt=0
for i in range(n):
    if lst[i+1]>lst[i+2]:
        x=min(lst[i],lst[i+1]-lst[i+2])
        cnt+=5*x
        lst[i]-=x
        lst[i+1]-=x
        y=min(lst[i],lst[i+1],lst[i+2])
        cnt+=7*y
        lst[i]-=y
        lst[i+1]-=y
        lst[i+2]-=y
    else:
        x=min(lst[i],lst[i+1],lst[i+2])
        cnt+=7*x
        lst[i]-=x
        lst[i+1]-=x
        lst[i+2]-=x
        y=min(lst[i],lst[i+1])
        cnt+=5*y
        lst[i]-=y
        lst[i+1]-=y
    cnt+=lst[i]*3
print(cnt)
