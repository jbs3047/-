n,m=map(int,input().split())
lst=[list(map(str,input())) for _ in range(n)]
chk=[["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"]]
ans=64
for i in range(n-7):
    for j in range(m-7):
        cnt=0
        for y in range(8):
            for x in range(8):
                if lst[i+y][j+x]==chk[y%2][x]:
                    cnt+=1

        if cnt>32:
            cnt=64-cnt
        if cnt<ans:
            ans=cnt

print(ans)