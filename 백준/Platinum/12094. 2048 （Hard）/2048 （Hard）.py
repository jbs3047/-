#12094 2048 (hard)
def go(x):
    if x==0:#up
        for j in range(n):
            check=0
            for i in range(1,n):
                if a[i][j]:
                    now=a[i][j]
                    a[i][j]=0
                    if a[check][j]==now:
                        a[check][j]=now*2
                        check+=1
                    elif a[check][j]==0:
                        a[check][j]=now
                    else:
                        check+=1
                        a[check][j]=now

    elif x==1:#down
        for j in range(n):
            check=n-1
            for i in range(n-2,-1,-1):
                if a[i][j]:
                    now=a[i][j]
                    a[i][j]=0
                    if a[check][j]==now:
                        a[check][j]=now*2
                        check-=1
                    elif a[check][j]==0:
                        a[check][j]=now
                    else:
                        check-=1
                        a[check][j]=now
    elif x==2:
        for i in range(n):
            check=0
            for j in range(1,n):
                if a[i][j]:
                    now=a[i][j]
                    a[i][j]=0
                    if a[i][check]==0:
                        a[i][check]=now
                    elif a[i][check]==now:
                        a[i][check]=now*2
                        check+=1
                    else:
                        check+=1
                        a[i][check]=now
    else:#right
        for i in range(n):
            check=n-1
            for j in range(n-2,-1,-1):
                if a[i][j]:
                    now=a[i][j]
                    a[i][j]=0
                    if a[i][check]==now:
                        a[i][check]=now*2
                        check-=1
                    elif a[i][check]==0:
                        a[i][check]=now
                    else:
                        check-=1
                        a[i][check]=now


def check(lsta,lstb):
    for i in range(n):
        for j in range(n):
            if lsta[i][j]!=lstb[i][j]:
                return True
    return False


def game(k):
    global a
    global mx
    global mn
    global n
    chk=0
    if k==10:
        for i in a:
            temp=max(i)
            if temp>mx:
                mx=temp
                for j in range(10,0,-1):
                    deep[j]=temp
                    temp//=2
        return
    for i in a:
        chk=max(chk,max(i))
    if deep[k]>=chk:
        return
    b=[item[:] for item in a]
    for i in range(4):
        go(i)
        if check(a,b):
            game(k+1)
            a=[item[:] for item in b]
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
deep=[0 for _ in range(11)]
cnt=0
for i in a:
    cnt=max(cnt,max(i))
mx=cnt
for i in range(10,0,-1):
    deep[i]=cnt
    cnt//=2
game(0)
print(mx)
