n=int(input())
a=[]
b=[]
c=[]
d=[]
for i in range(n):
    q,w,e,r=map(int,input().split())
    a.append(q)
    b.append(w)
    c.append(e)
    d.append(r)
left=[]
right=[]
for i in range(n):
    for j in range(n):
        left.append(a[i]+b[j])
        right.append(c[i]+d[j])
left.sort()
right.sort()
cnt=0
i=0
j=len(right)-1
while i<len(left) and j>=0:
    if left[i]+right[j]>0:
        j-=1
    elif left[i]+right[j]<0:
        i+=1
    else:
        chk1=1
        chk2=1
        while i+1<len(left) and left[i]==left[i+1]:
            chk1+=1
            i+=1
        while j-1>=0 and right[j]==right[j-1]:
            chk2+=1
            j-=1
        cnt+=chk1*chk2
        i+=1
        j-=1
print(cnt)