# 2630 색종이 만들기
import sys
input=sys.stdin.readline
n= int(input())
a=[list(map(int,input().split())) for _ in range(n)]

def quad(x,y,size):
    global n
    b=a[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if b!=a[i][j]:
                return quad(x,y,size//2)+quad(x,y+size//2,size//2)+quad(x+size//2,y,size//2)+quad(x+size//2,y+size//2,size//2)
    return str(a[x][y])
p=quad(0,0,n)
print(p.count('0'))
print(p.count('1'))