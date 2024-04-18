n=int(input())
lst=[list(map(str,input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]
dp2=[[0]*n for _ in range(n)]
def cal(left,str,right):
    if str=='+':
        return left+right
    elif str=='-':
        return left-right
    else:
        return left*right
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            lst[i][j]=int(lst[i][j])
dp[0][0]=lst[0][0]
dp2[0][0]=lst[0][0]
for i in range(2,n,2):
    dp[0][i]=cal(dp[0][i-2],lst[0][i-1],lst[0][i])
    dp[i][0]=cal(dp[i-2][0],lst[i-1][0],lst[i][0])
    dp2[0][i]=cal(dp2[0][i-2],lst[0][i-1],lst[0][i])
    dp2[i][0]=cal(dp2[i-2][0],lst[i-1][0],lst[i][0])
dp[1][1]=max(cal(dp[0][0],lst[1][0],lst[1][1]),cal(dp[0][0],lst[0][1],lst[1][1]))
dp2[1][1]=min(cal(dp2[0][0],lst[1][0],lst[1][1]),cal(dp2[0][0],lst[0][1],lst[1][1]))
for i in range(3,n):
    j=1
    dp[1][i]=max(cal(dp[1][i-2],lst[1][i-1],lst[1][i]),cal(dp[0][i-1],lst[0][i],lst[1][i]),cal(dp[0][i-1],lst[1][i-1],lst[1][i]))
    dp[i][1]=max(cal(dp[i-1][0],lst[i-1][1],lst[i][1]),cal(dp[i-1][0],lst[i][0],lst[i][1]),cal(dp[i-2][1],lst[i-1][1],lst[i][1]))
    dp2[1][i]=min(cal(dp2[1][i-2],lst[1][i-1],lst[1][i]),cal(dp2[0][i-1],lst[0][i],lst[1][i]),cal(dp2[0][i-1],lst[1][i-1],lst[1][i]))
    dp2[i][1]=min(cal(dp2[i-1][0],lst[i-1][1],lst[i][1]),cal(dp2[i-1][0],lst[i][0],lst[i][1]),cal(dp2[i-2][1],lst[i-1][1],lst[i][1]))
for i in range(2,n):
    for j in range(2,n):
        if (i+j)%2:
            continue
        dp[i][j]=max(cal(dp[i-2][j],lst[i-1][j],lst[i][j]),cal(dp[i-1][j-1],lst[i-1][j],lst[i][j]),cal(dp[i-1][j-1],lst[i][j-1],lst[i][j]),cal(dp[i][j-2],lst[i][j-1],lst[i][j]))
        dp2[i][j]=min(cal(dp2[i-1][j-1],lst[i-1][j],lst[i][j]),cal(dp2[i-1][j-1],lst[i][j-1],lst[i][j]),cal(dp2[i-2][j],lst[i-1][j],lst[i][j]),cal(dp2[i][j-2],lst[i][j-1],lst[i][j]))
print(dp[n-1][n-1],dp2[n-1][n-1])
# for i in dp:
#     print(i)
# print('===-=-=-=-=-')
# for i in dp2:
#     print(i)
