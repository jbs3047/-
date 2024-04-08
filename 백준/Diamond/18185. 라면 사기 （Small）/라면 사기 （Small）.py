# 3개짜리부터 먼저 -> 그다음 2개 -> 그다음 1개
# 2번째가 3번째보다 크고 4번째가 존재하는 경우 순서 고려 필요 (뒤3부터)
# 뒤3처리 되는경우 -> 앞이 2개처리 -> 앞에서 먼저 날려버리면 될거같은데
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
