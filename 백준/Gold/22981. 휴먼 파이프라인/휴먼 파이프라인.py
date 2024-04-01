n,k=map(int,input().split())
lst=[0]+list(map(int,input().split()))
lst.sort()
a=1
b=2
sm=0
while b<=n:
    ansa=lst[1]*a
    ansb=lst[b]*(n-a)
    sm=max(sm,ansa+ansb)
    a+=1
    b+=1
if k%sm==0:
    print(k//sm)
else:
    print(k//sm+1)