n=int(input())
lst1=[]
lst2=[]
for _ in range(n):
    a,b=map(int,input().split())
    lst1.append(a)
    lst2.append(b)
lst1.append(lst1[0])
lst2.append(lst2[0])
sm1=0
sm2=0
for i in range(n):
    sm1+=lst1[i]*lst2[i+1]
for i in range(n):
    sm2+=lst2[i]*lst1[i+1]

print('{:.1f}'.format(abs(sm1-sm2)/2))