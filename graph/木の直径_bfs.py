from collections import deque

N = int(input())
G = [list() for _ in range(N)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    G[a].append((b,c))
    G[b].append((a,c))

d = deque()
d.append(0)
dis = [-1]*N
d[0] = 0
while d:
    v = d.popleft()
    for nex, cost in G[v]:
        if dis[nex] == -1:
            dis[nex] = dis[v]+cost
            d.append(nex)
idx = dis.index(max(dis))
d.append(idx)
dis2 = [-1]*N
dis2[idx] = 0
p = [-1]*N
while d:
    v = d.popleft()
    for nex, cost in G[v]:
        if dis2[nex] == -1:
            dis2[nex] = dis2[v]+cost
            p[nex] = v
            d.append(nex)
idx2 = dis2.index(max(dis2))
ans = []
st, en = idx2, p[idx2]
while en!=-1:
    ans.append(st)
    st, en = en, p[en]
ans.append(st)
print(dis2[idx2], len(ans))
print(*ans)
