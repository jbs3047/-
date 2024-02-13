icp={"+":1,"-":1,"*":2,"/":2,"(":3}
isp={"+":1,"-":1,"*":2,"/":2,"(":0}
def get_postfix(infix,n):
    postfix=""

    stack=[]
    for i in range(n):
        if infix[i] not in "(+-*/)":
            postfix+=infix[i]
        else:
            if infix[i]==")":
                while stack:
                    c=stack.pop()
                    if c=="(":
                        break
                    else:
                        postfix+=c
            else:
                while stack and isp[stack[-1]]>=icp[infix[i]]:
                    postfix+=stack.pop()
                stack.append(infix[i])
    while stack: 
        postfix+=stack.pop()
    return postfix
asd=input()
ans=get_postfix(asd,len(asd))
print(ans)