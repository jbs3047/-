### 2110 공유기설치
n,c=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))
a.sort()

if c==2:
    print(a[-1]-a[0])
else:
    start=1
    end=(a[-1]-a[0])//(c-1)+1
    result=0

    while start<=end:
        mid=(start+end)//2
        first,count=a[0],1#맨 처음꺼 선택, 공유기 개수(맨 처음거 골랐으니 1)
    
        for i in range(n):
            if a[i]>=mid+first:
                first=a[i]
                count+=1
        if count>=c:
            start= mid+1
            result = mid
        else:
            end=mid-1
    print(result)