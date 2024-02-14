#10828 스택 - 시간초과
import sys
N = int(input())
b=[]
for i in range(N):
    #a=list(input().split())
    a= list(sys.stdin.readline().rstrip().split())
    if a[0] == 'push': #얘 뺴고 다 출력
        b.append(a[1])
    elif a[0] == 'pop':
        if len(b) == 0:
            print(-1)
        else:
            print(b[-1])
            del b[-1]
    elif a[0] == 'size':
        print(len(b))
    elif a[0] == 'empty':
        if len(b)==0:
            print(1)
        else:
            print(0)
    elif a[0] == 'top':
        if len(b)==0:
            print(-1)
        else:
            print(b[-1])
    
