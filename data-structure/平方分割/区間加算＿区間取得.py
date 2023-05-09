"""実装"""
# 更新処理の際に区間で足したところはself.add_dataに格納
# 一点取得の際にそのデータに格納されてる値と、
# その値が含まれる区間に足された値を足したものを返す


bucket_size = 350
class SqrtDecomposition:
    def __init__(self, N, init, func, ide):
        """
        平方分割して、各バケット内での値を計算
        """
        self.N = N
        self.data = []
        self.add_data = []
        self.func = func
        self.func_num = []
        d = []
        self.ide = ide
        if init==0:
            for i in range(bucket_size):
                self.data.append([ide]*bucket_size)
                self.add_data.append(0)
                self.func_num.append(ide)
        else:
            for i in range(self.N):
                if (i+1)%bucket_size==0:
                    d.append(init[i])
                    s = self.func(s,init[i])
                    self.data.append(d)
                    self.add_data.append(0)
                    self.func_num.append(s)
                    d = []
                    s = ide
                else:
                    d.append(init[i])
                    s = self.func(s,init[i])
            if d:
                self.data.append(d+[ide]*(bucket_size-len(d)))
                self.add_data.append(0)
                self.func_num.append(s)
    
    def add(self, l, r, x):
        """0-indexedの[l,r)にxを加算"""
        a1, b1 = l//bucket_size, l%bucket_size
        a2, b2 = r//bucket_size, r%bucket_size
        if a1==a2:
            for i in range(b1,b2):
                self.data[a1][i] += x
            # 更新処理
            s = self.ide
            for i in range(bucket_size):
                s = self.func(s,self.data[a1][i])
            self.func_num[a1] = s
        else:
            for i in range(b1, bucket_size):
                self.data[a1][i] += x
            for i in range(a1+1, a2):
                self.add_data[i] += x
            for i in range(b2):
                self.data[a2][i] += x
            # 更新処理
            s1, s2 = self.ide, self.ide
            for i in range(bucket_size):
                s1 = self.func(s1,self.data[a1][i])
                s2 = self.func(s2,self.data[a2][i])
            self.func_num[a1] = s1
            self.func_num[a2] = s2
    
    def get(self, i):
        """0-indexedのi番目を取得で計算"""
        a, b = i//bucket_size, i%bucket_size
        return self.data[a][b]+self.add_data[a]
    
    def query(self,l,r):
        """"区間[l,r)でfuncしたもの"""
        a1, b1 = l//bucket_size, l%bucket_size
        a2, b2 = r//bucket_size, r%bucket_size
        if a1==a2:
            res = self.ide
            for i in range(b1,b2):
                res = self.func(res,self.data[a1][i])
            return res+self.add_data[a1]
        else:
            res = self.ide
            for i in range(b1,bucket_size):
                res = self.func(res, self.data[a1][i]+self.add_data[a1])
            for i in range(b2):
                res = self.func(res, self.data[a2][i]+self.add_data[a2])
            for i in range(a1+1,a2):
                res = self.func(res, self.func_num[i]+self.add_data[i])
                # funcがsumの時は
                # res = self.func(res,self.func_num[i]+bucket_size*self.data[i])
            return res