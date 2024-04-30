from itertools import permutations
def game(lineup):
    batter=0
    score=0
    for inning in lst:
        out=0
        b1,b2,b3=0,0,0
        while True:
            if out==3:
                break
            if inning[lineup[batter]]==0: # out
                out+=1
            elif inning[lineup[batter]]==1: # 안타
                score+=b3
                b1,b2,b3=1,b1,b2
            elif inning[lineup[batter]]==2: # 2루타
                score+=(b3+b2)
                b1,b2,b3=0,1,b1
            elif inning[lineup[batter]]==3: # 3루타
                score+=(b1+b2+b3)
                b1,b2,b3=0,0,1
            else: # 홈런 굿
                score+=(b1+b2+b3+1)
                b1,b2,b3=0,0,0
            batter=(batter+1)%9
    return score


n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
ans=0

for lineup in permutations(range(1,9),8):
    lineup=list(lineup[:3])+[0]+list(lineup[3:])
    ans=max(ans,game(lineup))
print(ans)