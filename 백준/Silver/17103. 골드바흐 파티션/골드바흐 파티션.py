lst=[True]*(1000001)
m=int(1000000**0.5)
for i in range(2,m+1):
    if lst[i]==True:
        for j in range(2*i,1000000+1,i):
            lst[j]=False

t=int(input())
for i in range(t):
    n=int(input())
    cnt=0
    x=n//2
    y=n//2
    while x>=2:
        if lst[x]==True and lst[y]==True:
            cnt+=1
        x-=1
        y+=1
    print(cnt)
