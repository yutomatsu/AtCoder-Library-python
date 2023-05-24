# segtreeなどで操作をする際はHL分解してから
# data[order[i]]に値を代入する

class Heavy_Light_Decomposition:
    def __init__(self,N,G,root=0) -> None:
        self.N = N
        self.G = G
        self.size(root)
        self.hld(root)
    
    def size(self,root):
        """部分木サイズ、深さ、親を求める"""
        stack = [(root,1)]
        subtree = [0]*self.N
        depth = [0]*self.N
        parents = [-1]*self.N
        while stack:
            v,t = stack.pop()
            if t==1:
                stack.append((v,0))
                for nex in self.G[v]:
                    if nex==parents[v]:continue
                    parents[nex] = v
                    depth[nex] = depth[v]+1
                    stack.append((nex,1))
            else:
                subtree[v] = 1
                for nex in self.G[v]:
                    if nex==parents[v]:continue
                    subtree[v] += subtree[nex]
        self.subtree = subtree
        self.depth = depth
        self.parents = parents
    
    def hld(self,root):
        """HL分解"""
        order = [0]*self.N
        top = [0]*self.N
        heavy_c = [-1]*self.N
        stack = [root]
        num = 0
        while stack:
            v = stack.pop()
            order[v] = num
            num += 1
            max_c = 0
            for nex in self.G[v]:
                if nex!=self.parents[v] and max_c<self.subtree[nex]:
                    max_c = self.subtree[nex]
                    heavy_c[v] = nex
            for nex in self.G[v]:
                if nex!=self.parents[v] and nex!=heavy_c[v]:
                    top[nex] = nex
                    stack.append(nex)
            next_v = heavy_c[v]
            if next_v!=-1:
                top[next_v] = top[v]
                stack.append(next_v)
        self.order = order
        self.top = top 
    
    def query(self,u,v,edge=True):
        """
        u-v間の最短経路が通る分解後の閉区間を出力する。
        (個数はlog(N)で抑えられる)
        edge=Trueの時は重み付きグラフで子供から親に頂点を張る
        """
        res = []
        while self.top[u]!=self.top[v]:
            if self.order[u]<=self.order[v]:
                res.append([self.order[self.top[v]],self.order[v]])
                v = self.parents[self.top[v]]
            else:
                res.append([self.order[self.top[u]],self.order[u]])
                u = self.parents[self.top[u]]
        res.append([min(self.order[u],self.order[v])+(edge),max(self.order[u],self.order[v])])
        return res
    
    def query_each_vertex(self,u,v):
        """u-vパスの頂点集合列挙"""
        res = []
        while 1:
            if self.order[u]>self.order[v]:
                u,v = v,u
            res.append([max(self.order[self.top[v]],self.order[u]),self.order[v]])
            if self.top[u]!=self.top[v]:
                v = self.parents[self.top[v]]
            else:
                return res
    
    def query_each_edge(self,u,v):
        """重みありの時"""
        res = []
        while 1:
            if self.order[u]>self.order[v]:
                u,v = v,u
            if self.top[u]!=self.top[v]:
                res.append([self.order[self.top[v]],self.order[v]])
                v = self.parents[self.top[v]]
            else:
                if u!=v:
                    res.append([self.order[u]+1,self.order[v]])
                return res
    
    def lca(self,u,v):
        while 1:
            if self.order[u]>self.order[v]:
                u,v = v,u
            if self.top[u]==self.top[v]:
                return u
            v = self.parents[self.top[v]]

N = int(input())
G = [list() for _ in range(N)]
p = list(map(int, input().split()))
for i in range(N):
    if p[i]==-1:
        continue
    G[p[i]].append(i)
    G[i].append(p[i])
hld = Heavy_Light_Decomposition(N,G)
res = hld.query(4,9)
for l,r in res:
    pass
    # segtreeでなんとかみたいな操作でパス上の最小値とかがわかる

# パス上に沿ってクエリを処理したい時は
def forward(x,y):
    """f_y(f_x())みたいな感じ"""
    return 
def backward(x,y):
    """f_x(f_y())"""
    return forward(y,x)

# 参考 https://judge.yosupo.jp/submission/25696
u,v = 0,7
lca = hld.lca(u,v)
for l,r in hld.query_each_edge(lca,u):
    backward(l,r+1)
    # segtreeとかの処理
    pass
for l,r in hld.query_each_vertex(lca,v):
    forward(l,r+1)
    pass
# みたいな感じ
