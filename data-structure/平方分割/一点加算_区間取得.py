# https://kujira16.hateblo.jp/entry/2016/12/15/000000

"""
一点加算
区間(min, max, sum)
ide = float('inf'), 0, 0
"""

# 各バケット内の数
bucket_size = 3
class SqrtDecomposition:
    def __init__(self, N, init, func, ide):
        """
        平方分割して、各バケット内での値を計算
        """
        self.N = N
        self.data = []
        self.func_num = []
        self.func = func
        self.ide = ide
        d = []
        s = ide
        if init==0:
            for i in range(bucket_size):
                self.data.append([ide]*bucket_size)
                self.func_num.append(ide)
        else:
            for i in range(self.N):
                if (i+1)%bucket_size==0:
                    d.append(init[i])
                    s = self.func(s, init[i])
                    self.data.append(d)
                    self.func_num.append(s)
                    d = []
                    s = ide
                else:
                    d.append(init[i])
                    s = self.func(s, init[i])
            if d:
                self.data.append(d+[ide]*(bucket_size-len(d)))
                self.func_num.append(s)
    
    def add(self, i, x):
        """0-indexedのi番目にxを加算"""
        a, b = i//bucket_size, i%bucket_size
        self.data[a][b] += x
        # max, min等の場合の処理は以下で大丈夫だが、sumなどはself.data[a][b]->xに変更
        self.func_num[a] = self.func(self.func_num[a], self.data[a][b])
    
    def query(self, l, r):
        """0-indexedの区間[l,r)で計算"""
        a1, b1 = l//bucket_size, l%bucket_size
        a2, b2 = r//bucket_size, r%bucket_size
        res = self.ide
        if a1==a2:
            for i in range(b1, b2):
                res = self.func(res, self.data[a1][i])
            return res
        for i in range(b1, bucket_size):
            res = self.func(self.data[a1][i], res)
        for i in range(a1+1, a2):
            res = self.func(self.func_num[i], res)
        for i in range(b2):
            res = self.func(self.data[a2][i], res)
        return res

s = SqrtDecomposition(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 20], lambda x, y:x+y, 0)
print(1)