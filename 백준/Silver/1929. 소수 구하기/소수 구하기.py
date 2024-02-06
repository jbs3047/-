##1929 소수 구하기
import sys
a, b = map(int,sys.stdin.readline().rstrip().split())
#a, b = map(int,input().split())
c=[]
for i in range(a,b+1):
    k=0
    if i == 1:
        k +=1
    for j in range(2,int((i**0.5)+1)):
        if i%j ==0:
            k +=1
            break
    if k ==0:
        c.append(i)

for i in range(len(c)):
    print(c[i])