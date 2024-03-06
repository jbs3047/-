import heapq

n = int(input())
vis = [0 for _ in range(n)]
ans = 0
lst = [[] for _ in range(n)]
chk = []
for i in range(n):
    a, b, c = map(int, input().split())
    chk.append([a, b, c, i])
# 간선이 n-1개만 필요하니까 그 다음 가중치 애들은 날려버려야함
# 어짜피 스패닝트리 구조가 인접한거만 연결하는거같은데 인접만 확인하고 넣으면 되지않을까
chk.sort(key=lambda x: x[0])
for i in range(n):
    a, b, c, p = chk[i]
    if i != n - 1:
        d, e, f, u = chk[i + 1]
    else:
        d, e, f, u = chk[0]
    q, w, r, o = chk[i - 1]
    x = abs(d - a)
    y = abs(q - a)
    lst[p].append([x,u])
    lst[p].append([y,o])
chk.sort(key=lambda x: x[1])
for i in range(n):
    a, b, c, p = chk[i]
    if i != n - 1:
        d, e, f, u = chk[i + 1]
    else:
        d, e, f, u = chk[0]
    q, w, r, o = chk[i - 1]
    x = abs(e - b)
    y = abs(w - b)
    lst[p].append([x,u])
    lst[p].append([y,o])
chk.sort(key=lambda x: x[2])
for i in range(n):
    a, b, c, p = chk[i]
    if i != n - 1:
        d, e, f, u = chk[i + 1]
    else:
        d, e, f, u = chk[0]
    q, w, r, o = chk[i - 1]
    x = abs(f - c)
    y = abs(r - c)
    lst[p].append([x,u])
    lst[p].append([y,o])
heap = [[0, 0]]
while heap:
    w, now = heapq.heappop(heap)
    if not vis[now]:
        vis[now] = 1
        ans += w
        for next in lst[now]:
            heapq.heappush(heap, next)
print(ans)
