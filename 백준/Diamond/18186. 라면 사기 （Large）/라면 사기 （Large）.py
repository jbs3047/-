n,b,c=map(int,input().split())
lst=list(map(int,input().split()))+[0,0]
cnt=0
if c>=b:
    print(sum(lst)*b)
else:
    for i in range(n):
        if lst[i+1]>lst[i+2]:
            x=min(lst[i],lst[i+1]-lst[i+2])
            cnt+=(b+c)*x
            lst[i]-=x
            lst[i+1]-=x
            y=min(lst[i],lst[i+1],lst[i+2])
            cnt+=(b+c+c)*y
            lst[i]-=y
            lst[i+1]-=y
            lst[i+2]-=y
        else:
            x=min(lst[i],lst[i+1],lst[i+2])
            cnt+=(b+c+c)*x
            lst[i]-=x
            lst[i+1]-=x
            lst[i+2]-=x
            y=min(lst[i],lst[i+1])
            cnt+=(b+c)*y
            lst[i]-=y
            lst[i+1]-=y
        cnt+=lst[i]*b
    print(cnt)
