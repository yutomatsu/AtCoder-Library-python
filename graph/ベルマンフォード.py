# 計算量 O(N*M)

N, M = map(int, input().split())
edge = []
for i in range(M):
    u, v, w = map(int, input().split())
    edge.append([u, v, w])

# 最短距離
d = [float('inf')]*N

# 始点s
def bellman(s):
    d[s] = 0
    while True:
        update = False
        for i in range(M):
            e = edge[i]
            if d[e[0]] != float('inf') and d[e[1]] > d[e[0]]+e[2]:
                d[e[1]] = d[e[0]] + e[2]
                update = True
        if not update:
            break

# 負閉路検出
def find_negative_roop():
    d = [0]*N
    for i in range(N):
        for j in range(M):
            e = edge[j]
            if d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                # n回目に更新ありなら負閉路
                if i == N-1:
                    return True
    return False

# 最短距離と負閉路検出
# 負閉路あれば-infに
def bellmanford(s):
    d = [float('inf')] * N
    d[s] = 0
    for i in range(N):
        for j in range(M):
            e = edge[j]
            if d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                # n回目にも更新があるなら負の経路が存在する
                if i == N-1:
                    d[e[1]] = -float('inf')
                    while True:
                        update = False
                        for i in range(M):
                            e = edge[i]
                            if d[e[1]] != -float('inf') and d[e[0]] == -float('inf'):
                                d[e[1]] = -float('inf')
                                update = True
                        if not update:
                            break
    return d

bellman(0)
print(d)