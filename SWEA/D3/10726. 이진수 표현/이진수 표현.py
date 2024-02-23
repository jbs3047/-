t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    ans="0"*31+bin(m)
    cnt=0
    for i in range(n):
        if ans[-1-i]=="1":
            cnt+=1
    if cnt==n:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')