# 参考
# https://qiita.com/Kiri8128/items/a011c90d25911bdb3ed3#bottom-up-dp

# https://atcoder.jp/contests/dp/tasks/dp_v
class Rerooting:
    def __init__(self,n,G) -> None:
        """
        n:頂点数
        G:隣接リスト
        """
        self.n = n
        self.G = G
    
    def solve(self,f_bu,f_td,g,merge,ide,root=0):
        # orderを求める
        parents = [-1]*self.n
        order = []
        stack = [root]
        while stack:
            v = stack.pop()
            order.append(v)
            for nex in self.G[v]:
                if nex==parents[v]:continue
                parents[nex] = v
                stack.append(nex)
        
        # bottom up
        """
        根をrootに固定した時、根でない頂点iについて、
        親をp_i,子の集合をC_iとして、
        acc[i] = merge({res[c]}|c belong to C_i)
        """
        res = [ide]*self.n
        acc_BU = [ide]*self.n
        for v in order[::-1]:
            if v!=root:
                p = parents[v]
                # 親側へ更新する時の調整。マージ結果に何を加えるか
                res[v] = f_bu(acc_BU[v],v)
                acc_BU[p] = merge(acc_BU[p],res[v])
            else:
                # rootへの操作
                res[v] = g(acc_BU[v],v)
        
        # top down
        TD = [ide]*self.n
        for v in order:
            acc = TD[v]
            for nex in self.G[v]:
                if nex==parents[v]:continue
                TD[nex] = acc
                acc = merge(acc,res[nex])
            acc = ide
            for nex in self.G[v][::-1]:
                if nex==parents[v]:continue
                TD[nex] = f_td(merge(TD[nex],acc),nex,v)
                acc = merge(acc,res[nex])
                res[nex] = g(merge(acc_BU[nex],TD[nex]),nex)
        
        return res

# ABC222 F
# 重みあり
# https://atcoder.jp/contests/abc222/tasks/abc222_f
class Rerooting:
    def __init__(self,n,G) -> None:
        """
        n:頂点数
        G:隣接リスト
        """
        self.n = n
        self.G = G
    
    def solve(self,f_bu,f_td,g,merge,ide,root=0):
        # orderを求める
        parents = [-1]*self.n
        # 重みあり
        w = [0]*self.n
        order = []
        stack = [root]
        while stack:
            v = stack.pop()
            order.append(v)
            for nex,cost in self.G[v]:
                if nex==parents[v]:continue
                parents[nex] = v
                # 重みあり
                w[nex] = cost
                stack.append(nex)
        
        # bottom up
        res = [ide]*self.n
        acc_BU = [ide]*self.n
        for v in order[::-1]:
            p = parents[v]
            if v!=root:
                res[v] = f_bu(acc_BU[v],v)+w[v]
                acc_BU[p] = merge(acc_BU[p],res[v])
            else:
                res[v] = g(acc_BU[v],v)
        
        # print(*res)
        # print(*acc_BU)

        # top down
        TD = [ide]*self.n
        for v in order:
            acc = TD[v]
            for nex,_ in self.G[v]:
                if nex==parents[v]:
                    continue
                else:
                    TD[nex] = acc
                    acc = merge(acc,res[nex])
            acc = ide
            for nex,_ in self.G[v][::-1]:
                if nex==parents[v]:
                    continue
                else:
                    TD[nex] = f_td(merge(TD[nex],acc),v,nex)+w[nex]
                    acc = merge(acc,res[nex])
        
        # print(*TD)
        for i in range(N):
            res[i] = g(merge(acc_BU[i],TD[i]),i)    
        return res

def f_bu(a,v):
    """親方向へマージする時の調整"""
    return max(a,D[v])
def f_td(a,v,p):
    """子方向へマージする時の調整"""
    return max(a,D[v])
def g(a,v):
    """最終調整"""
    return a
def merge(v,nv):
    """マージ関数"""
    return max(v,nv)
