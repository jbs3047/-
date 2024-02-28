import sys
input=sys.stdin.readline
a=int(input())
dpmx=[0,0,0]
dpmn=[0,0,0]
lst=list(map(int,input().split()))

dpmx=lst[:]
dpmn=lst[:]
for i in range(1,a):
    lst=list(map(int,input().split()))
    q=dpmx[0]
    w=dpmx[1]
    e=dpmx[2]
    r=dpmn[0]
    t=dpmn[1]
    y=dpmn[2]
    dpmx[0]= max(q,w)+lst[0]
    dpmx[1]= max(q,w,e)+lst[1]
    dpmx[2]= max(w,e)+lst[2]
    dpmn[0]= min(r,t)+lst[0]
    dpmn[1]= min(r,t,y)+lst[1]
    dpmn[2]= min(t,y)+lst[2]
print(max(dpmx),min(dpmn))