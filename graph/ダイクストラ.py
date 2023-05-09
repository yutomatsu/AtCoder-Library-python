# 計算量 O(M*logN)

from heapq import heappush, heappop
INF = float('inf')

def dijkstra(s, n):
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    # 経路復元用
    prev = [-1]*n
    while hq:
        dis, v = heappop(hq)
        if dist[v] < dis:
            continue
        seen[v] = True
        for to, cost in G[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                prev[to] = v
                heappush(hq, (dist[to], to))
    return dist, prev

# 経路の最大辺除くを1回除ける時のダイクストラ
def dijkstra(s, n):
    dist = [[INF] * 2 for _ in range(n)]
    hq = [(0, 0, s)]
    dist[s][0] = 0
    dist[s][1] = 0
    while hq:
        # vまでの距離、辺を除く処理を行ったかどうか、現在の頂点
        d, ticket, v = heappop(hq)
        if d > dist[v][ticket]:
            continue
        # vからつながる点について
        for to, cost in G[v]:
            # 短ければ更新
            if dist[v][ticket] + cost < dist[to][ticket]:
                dist[to][ticket] = d + cost
                # prev[to] = v
                heappush(hq, (dist[to][ticket], ticket, to))
            # 辺を除く処理行っていない時は除いた時の処理を格納
            if ticket == 0:
                if dist[to][1] > d:
                    dist[to][1] = d
                    heappush(hq, (d, 1, to))
    return dist

G = [list() for _ in range(4)]