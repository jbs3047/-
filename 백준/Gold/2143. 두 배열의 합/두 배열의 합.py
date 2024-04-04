t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
left=[]
for i in range(n-1):
    x=a[i]
    left.append(x)
    for j in range(i+1,n):
        x+=a[j]
        left.append(x)
left.append(a[-1])
right=[]
for i in range(m-1):
    x=b[i]
    right.append(x)
    for j in range(i+1,m):
        x+=b[j]
        right.append(x)
right.append(b[-1])
left.sort()
right.sort()
i=0
j=len(right)-1
cnt=0
while i<len(left) and j>=0:
    if left[i]+right[j]>t:
        j-=1
    elif left[i]+right[j]<t:
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