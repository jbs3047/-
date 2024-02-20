def garo():
    global ans
    for y in range(n):
        now=lst[y][0]
        cnt=1
        chk=0
        for x in range(1,n):
            if lst[y][x]>now:#오르막
                if cnt >= c and lst[y][x]==now+1:
                    now = lst[y][x]
                    cnt = 1
                else:
                    chk = 1
                    break
            elif lst[y][x]<now:#내리막
                fnd=0
                cnt=1
                for i in range(x,x+c):
                    if i<n and lst[y][i]==now-1:
                        fnd+=1
                if fnd!=c:
                    chk=1
                    break
                now=lst[y][x]
                cnt-=c
            else:
                cnt+=1
        if chk==0:
            #print(y)
            ans+=1
def sero():
    global ans
    for x in range(n):
        now=lst[0][x]
        cnt=1
        chk=0
        for y in range(1,n):
            if lst[y][x]>now:#오르막
                if cnt>=c and lst[y][x]==now+1:
                    now=lst[y][x]
                    cnt=1
                else:
                    chk=1
                    break
            elif lst[y][x]<now:#내리막
                cnt=1
                fnd=0
                for i in range(y,y+c):
                    if i<n and lst[i][x]==now-1:
                        fnd+=1
                if fnd!=c:
                    chk=1
                    break
                now=lst[y][x]
                cnt-=c
            else:
                cnt+=1
        if chk==0:
            #print(x)
            ans+=1
n,c=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
ans=0
garo()
sero()
print(ans)