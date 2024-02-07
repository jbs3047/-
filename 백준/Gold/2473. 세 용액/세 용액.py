import sys
def sol():
    if a[0]>=0:
        print(a[0],a[1],a[2])
        return
    elif a[-1]<=0:
        print(a[-3],a[-2],a[-1])
        return
    c=3000000001
    for i in range(n-2):
        s=i+1
        e=n-1
        while s<e:
            x=a[i]+a[s]+a[e]
            if x==0:
                print(a[i],a[s],a[e])
                return
            y=abs(x)
            if y<c:
                c=y
                p,q,r=a[i],a[s],a[e]
            if x>0:
                e-=1
            else:
                s+=1
         
    print(p,q,r)
    return

n=int(sys.stdin.readline())
a=sorted(list(map(int,sys.stdin.readline().split())))
sol()