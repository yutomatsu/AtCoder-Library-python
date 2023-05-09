import sys
sys.setrecursionlimit(10**8)
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")

class LCA:
    """
    前処理O(nlogn)、クエリO(logn)
    木上の任意の2点のLCAを求める
    """
    def __init__(self, N, G, root = 0) -> None:
        """頂点数:N、辺情報:G、根のidx:root dabulingで前処理を行う"""
        self.G = G
        self.depth = [-1]*N
        self.dist = [-1]*N
        self.ancestors = [[-1]*(N+1)]
        self.depth[root] = 0
        self.dist[root] = 0
        self.dfs(root,-1)
        max_d = max([self.depth[i] for i in range(N)])

        # doubling前処理
        # 各頂点についてk=0,1,2,,,に対する2^k個先の親を求める
        d = 1
        prev = self.ancestors[0]
        while d<max_d:
            nex = [prev[i] for i in prev]
            self.ancestors.append(nex)
            d <<= 1
            prev = nex

    def dfs(self,v,p):
        for nex, cost in self.G[v]:
            if nex==p:continue
            self.depth[nex] = self.depth[v]+1
            self.dist[nex] = self.dist[v]+cost
            self.ancestors[0][nex] = v
            self.dfs(nex,v)
    
    def lca_query(self, u, v):
        """u,vの最小共通祖先を求める"""
        du, dv = self.depth[u], self.depth[v]
        if du>dv:
            u, v = v, u
            du, dv = dv, du
        # vを同じ高さまで上げる
        diff, idx = dv-du, 0
        while diff:
            if diff&1:
                v = self.ancestors[idx][v]
            diff >>= 1
            idx += 1
        if u==v:
            return u
        for i in range(len(bin(du)[2:])-1,-1,-1):
            pu, pv = self.ancestors[i][u], self.ancestors[i][v]
            if pu!=pv:
                u, v = pu, pv
        assert self.ancestors[0][u]==self.ancestors[0][v]
        return self.ancestors[0][u]
    
    def dist_query(self, u, v):
        """u,vの最小共通祖先を求めて距離を出す"""
        lca = self.lca_query(u, v)
        return self.dist[u]+self.dist[v]-2*self.dist[lca]

"""使い方"""
N = int(input())
G = [list() for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append((b,1))  # <-重みも
    G[b].append((a,1))

lca = LCA(N,G)