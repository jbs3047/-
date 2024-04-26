#14468 소가 길을 건너간 이유 2
x=str(input())
stack=[]
chk=[0 for _ in range(26)]
cnt=0
for i in range(52):
    if not stack:
        stack.append(x[i])
        chk[ord(x[i])-65]+=1
    else:
        if stack[-1]==x[i]:
            stack.pop()
        else:
            if not chk[ord(x[i])-65]:
                chk[ord(x[i])-65]+=1
                stack.append(x[i])
            else:
                chk[ord(x[i]) - 65] += 1
                for j in range(len(stack)-1,-1,-1):
                    if stack[j]!=x[i]:
                        cnt+=1
                    else:
                        del stack[j]
                        break
print(cnt)