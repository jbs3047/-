x=str(input())
y=str(input())
stack=[]
for i in range(len(x)):
    stack.append(x[i])
    if len(stack)<len(y):
        continue
    cnt=0
    for j in range(len(y)):
        chky=y[-1-j]
        chkx=stack[-1-j]
        if chkx==chky:
            cnt+=1
        if cnt==len(y):
            for k in range(len(y)):
                stack.pop()
if stack:
    for i in stack:
        print(i,end='')
else:
    print('FRULA')
