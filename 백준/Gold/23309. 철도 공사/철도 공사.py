# 23309 철도 공사

n,m=map(int,input().split())
lst=list(map(int,input().split()))
prev=[0]*1000001
next=[0]*1000001
ans=[]
for i in range(n):
    prev[lst[i]]=lst[i-1]
    next[lst[i-1]]=lst[i]
for _ in range(m):
    line=list(map(str,input().split()))
    if line[0]=="BN":
        i,j=int(line[1]),int(line[2])
        ans.append(next[i])
        nxt=next[i]
        next[j]=nxt
        prev[j]=i
        next[i]=j
        prev[nxt]=j
    elif line[0]=="BP":
        i,j=int(line[1]),int(line[2])
        ans.append(prev[i])
        prv=prev[i]
        next[j]=i
        prev[j]=prv
        next[prv]=j
        prev[i]=j
    elif line[0]=="CN":
        i=int(line[1])
        ans.append(next[i])
        nxt=next[i]
        nnxt=next[nxt]
        next[i]=nnxt
        prev[nnxt]=i
    else:
        i=int(line[1])
        ans.append(prev[i])
        prv=prev[i]
        pprv=prev[prv]
        next[pprv]=i
        prev[i]=pprv
for i in ans:
    print(i)