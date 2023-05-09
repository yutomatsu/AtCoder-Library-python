class Binary_Indexed_Tree:
    def __init__(self, n) -> None:
        self._n = n
        self.data = [0] * (n+1)
        self.depth = n.bit_length()

    def add(self, p, x) -> None:
        """0-indexのp番目にxを加算"""
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p-1] += x
            p += p & (-p)
    
    def sum(self, l, r) -> int:
        """区間[l,r)で計算"""
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)
    
    def _sum(self, d) -> int:
        sm = 0
        while d > 0:
            sm += self.data[d-1]
            d -= d & (-d)
        return sm
    
    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self._n and sum_ + self.data[k-1] < x:
                sum_ += self.data[k-1]
                pos += 1 << i
        return pos, sum_

class RangeAddSum:
    def __init__(self,N) -> None:
        self.N = N
        self.bit1 = Binary_Indexed_Tree(N)
        self.bit2 = Binary_Indexed_Tree(N)
    
    def add(self,l,r,x):
        """[l,r) <- add x"""
        self.bit1.add(l,-x*(l-1))
        self.bit1.add(r-1,x*(r-1))
        self.bit2.add(l,x)
        self.bit2.add(r-1,-x)
    
    def sum(self,l,r):
        """return sum[l,r)"""
        return self.bit2._sum(r)*(r-1)+self.bit1._sum(r)-self.bit2.sum(l)*(l-1)-self.bit1._sum(l)
