def cal(lst,ans):
    if sum(lst)==0:
        for i in ans:
            print(i,end='')
        print()

    for i in range(26):
        if lst[i]:
            lst[i]-=1
            ans.append(chr(i+97))
            cal(lst,ans)
            ans.pop()
            lst[i]+=1
n=int(input())
for _ in range(n):
    lst=[0 for _ in range(26)]
    x=str(input())
    for i in x:
        lst[ord(i)-97]+=1
    cal(lst,[])