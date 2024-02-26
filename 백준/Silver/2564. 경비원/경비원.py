x,y=map(int,input().split())
n=int(input())
lst=[[] for _ in range(n)]
ans=0
for i in range(n):
    a,b=map(int,input().split())
    lst[i]=[a,b]
# 1 북 2 남 3 서 4 동
dx,dy=map(int,input().split())
for j in lst:
    if dx*j[0]==2 or dx*j[0]==12:
        if dx <=2:
            ans+=min(dy+j[1],2*x-(dy+j[1]))+y
        else:
            ans+=min(dy+j[1],2*y-(dy+j[1]))+x
    else: # 옆쪽, 동근 짝 홀 구분,좌우 구분 , 같은라인은?
        if dx==j[0]:
            ans+=abs(dy-j[1])
        else:
            if dx==1:
                if j[0]==3:
                    ans+=dy+j[1]
                else:
                    ans+=x-dy+j[1]
            elif dx==2:#남
                if j[0]==3:
                    ans+=dy+y-j[1]
                else:
                    ans+=x-dy+y-j[1]
            elif dx==3:#서
                if j[0]==1:
                    ans+=dy+j[1]
                else:
                    ans+=y-dy+j[1]
            else:#동
                if j[0]==1:
                    ans+=dy+x-j[1]
                else:  
                    ans+=y-dy+x-j[1]

print(ans)