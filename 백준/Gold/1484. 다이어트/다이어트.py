n=int(input())
start=1
end=1
ans=[]
while start<=n and end<=n:
    if end**2-start**2==n:
        ans.append(end)
    if end**2 - start**2 <n:
        end+=1
    else:
        start+=1
if ans:
    for i in ans:
        print(i)
else:
    print(-1)