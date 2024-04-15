lc1=[""]+list(map(str,input()))
lc2=[""]+list(map(str,input()))
y=len(lc1)
x=len(lc2)
lst=[[0]*(x+1) for _ in range(y+1)]
for i in range(1,y):
    for j in range(1,x):
        if lc1[i]==lc2[j]:
            lst[i][j]=lst[i-1][j-1]+1
        else:
            lst[i][j]=max(lst[i-1][j],lst[i][j-1])

print(lst[y-1][x-1])
