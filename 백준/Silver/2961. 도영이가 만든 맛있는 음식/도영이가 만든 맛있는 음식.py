from itertools import combinations
n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
mn=1000000000
for i in range(1,n+1):
    for j in combinations(lst,i):
        s=1
        b=0
        for k in range(i):
            s*=j[k][0]
            b+=j[k][1]
        mn=min(mn,abs(s-b))
print(mn)