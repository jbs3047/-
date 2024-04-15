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
#for i in lst:
#    print(i)

print(lst[y-1][x-1])
ans=''
i=y-1
j=x-1
while i>0 and j>0:
    if lc1[i]==lc2[j]:
        ans=lc1[i]+ans
        if len(ans)==lst[y-1][x-1]:
            break
        i-=1
        j-=1
    else:
        if lst[i-1][j]>lst[i][j-1]:
            i-=1
        else:
            j-=1
print(ans)
# i=1
# j=1
# ans2=''
# while i<y and j<x:
#     if lc1[i]==lc2[j]:
#         ans2+=lc1[i]
#         if len(ans2)==lst[y-1][x-1]:
#             break
#         i+=1
#         j+=1
#     else:
#         if lst[i+1][j]>lst[i][j+1]:
#             i+=1
#         else:
#             j+=1
# print(ans2)