#14465 소가 길을 건너간 이유 5

n,k,b=map(int,input().split())
lst=[1 for _ in range(n)]
for i in range(b):
    lst[int(input())-1]=0

cnt=k+1
i=0
sm=sum(lst[0:k])
while i+k<=len(lst):
    cnt=min(cnt,k-sm)
    if i+k==len(lst):
        break
    sm-=lst[i]
    sm+=lst[i+k]
    i+=1
print(cnt)