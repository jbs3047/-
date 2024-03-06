from itertools import combinations
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
answer = 10 ** 6
chk = [i for i in range(n)]
for c in combinations(chk, n // 2):
    cnt1 = 0
    cnt2 = 0
    ans = list(c)
    ans2 = [i for i in chk if i not in ans]
    for i in range(n // 2):
        for j in range(n // 2):
            cnt1 += lst[ans[i]][ans[j]]
            cnt2 += lst[ans2[i]][ans2[j]]
    if abs(cnt2 - cnt1) < answer:
        answer = abs(cnt2 - cnt1)
print(answer)