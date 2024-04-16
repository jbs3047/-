##### 14500 테트로미노
max=0
n,m=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]

def find():
    global max
    for i in range(n-1): #네모 1
        for j in range(m-1):
            sum=lst[i][j]+lst[i+1][j]+lst[i][j+1]+lst[i+1][j+1]
            if sum>max:
                max=sum
    for i in range(n): #ㅡ 2
        for j in range(m-3):
            sum=lst[i][j]+lst[i][j+1]+lst[i][j+2]+lst[i][j+3]
            if sum>max:
                max=sum
    for i in range(n-3): #ㅣ 3
        for j in range(m):
            sum=lst[i][j]+lst[i+1][j]+lst[i+2][j]+lst[i+3][j]
            if sum>max:
                max=sum
    for i in range(n-2): #번개 왼위 4
        for j in range(m-1):
            sum=lst[i][j]+lst[i+1][j]+lst[i+1][j+1]+lst[i+2][j+1]
            if sum>max:
                max=sum
    for i in range(n-2): #번개  오른위 5
        for j in range(1,m):
            sum=lst[i][j]+lst[i+1][j]+lst[i+1][j-1]+lst[i+2][j-1]
            if sum>max:
                max=sum
    for i in range(n-1): #번개 누움 오른위 6
        for j in range(1,m-1):
            sum=lst[i][j]+lst[i][j+1]+lst[i+1][j]+lst[i+1][j-1]
            if sum>max:
                max=sum
    for i in range(n-1): #번개 누움 왼위 7
        for j in range(m-2):
            sum=lst[i][j]+lst[i][j+1]+lst[i+1][j+1]+lst[i+1][j+2]
            if sum>max:
                max=sum
    for i in range(n-2): #ㅓ 8
        for j in range(1,m):
            sum=lst[i][j]+lst[i+1][j]+lst[i+1][j-1]+lst[i+2][j]
            if sum>max:
                max=sum
    for i in range(n-2): #ㅏ 9
        for j in range(m-1):
            sum=lst[i][j]+lst[i+1][j]+lst[i+1][j+1]+lst[i+2][j]
            if sum>max:
                max=sum
    for i in range(n-1): #ㅗ 10
        for j in range(1,m-1):
            sum=lst[i][j]+lst[i+1][j-1]+lst[i+1][j]+lst[i+1][j+1]
            if sum>max:
                max=sum
    for i in range(n-1): #ㅜ 11
        for j in range(1,m-1):
            sum=lst[i][j]+lst[i][j-1]+lst[i][j+1]+lst[i+1][j]
            if sum>max:
                max=sum
    for i in range(n-2): #ㄴ 12
        for j in range(m-1):
            sum=lst[i][j]+lst[i+1][j]+lst[i+2][j]+lst[i+2][j+1]
            if sum>max:
                max=sum
    for i in range(n-1): #13
        for j in range(2,m):
            sum=lst[i][j]+lst[i+1][j]+lst[i+1][j-1]+lst[i+1][j-2]
            if sum>max:
                max=sum
    for i in range(n-2): #14
        for j in range(m-1):
            sum=lst[i][j]+lst[i][j+1]+lst[i+1][j+1]+lst[i+2][j+1]
            if sum>max:
                max=sum
    for i in range(n-1): #15 - 반시계방향 90도씩 회전
        for j in range(m-2):
            sum=lst[i][j]+lst[i][j+1]+lst[i][j+2]+lst[i+1][j]
            if sum>max:
                max=sum
    for i in range(n-2): #ㄴ 뒤집기 16
        for j in range(1,m):
            sum=lst[i][j]+lst[i+1][j]+lst[i+2][j]+lst[i+2][j-1]
            if sum>max:
                max=sum
    for i in range(n-1): #17
        for j in range(m-2):
            sum=lst[i][j]+lst[i][j+1]+lst[i][j+2]+lst[i+1][j+2]
            if sum>max:
                max=sum
    for i in range(n-2): #18
        for j in range(m-1):
            sum=lst[i][j]+lst[i][j+1]+lst[i+1][j]+lst[i+2][j]
            if sum>max:
                max=sum
    for i in range(n-1): #19 -반시계방향 90도씩 회전
        for j in range(m-2):
            sum=lst[i][j]+lst[i+1][j]+lst[i+1][j+1]+lst[i+1][j+2]
            if sum>max:
                max=sum
    
find()
print(max)