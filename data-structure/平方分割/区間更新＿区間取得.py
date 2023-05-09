# minとかmaxなら

bucket_size = 350
class SqrtDecomposition:
    def __init__(self, N, init, func, ide):
        """
        平方分割して、各バケット内での値を計算
        """
        self.N = N
        self.data = []
        self.lazydata = []
        self.func_num = []
        self.func = func
        self.ide = ide
        d = []
        if init==0:
            for i in range(bucket_size):
                self.data.append([ide]*bucket_size)
                self.lazydata.append(None)
                self.func_num.append(ide)
        else:
            for i in range(self.N):
                if (i+1)%bucket_size==0:
                    d.append(init[i])
                    s = self.func(s,init[i])
                    self.data.append(d)
                    self.lazydata.append(None)
                    self.func_num.append(s)
                    d = []
                    s = ide
                else:
                    d.append(init[i])
                    s = self.func(s,init[i])
            if d:
                self.data.append(d+[ide]*(bucket_size-len(d)))
                self.lazydata.append(None)
                self.func_num.append(s)
    
    def update(self, l, r, x):
        """0-indexedの[l,r)にxで更新"""
        # 更新処理をかく
        a1, b1 = l//bucket_size, l%bucket_size
        a2, b2 = r//bucket_size, r%bucket_size
        if a1==a2:
            s = self.ide
            for i in range(bucket_size):
                if b1<=i<b2:
                    self.data[a1][i] = x
                else:
                    if self.lazydata[a1]!=None:
                        self.data[a1][i] = self.lazydata[a1]
                s = self.func(s,self.data[a1][i])
            self.func_num[a1] = s
            self.lazydata[a1] = None
        else:
            s1 = self.ide
            for i in range(bucket_size):
                if i>=b1:
                    self.data[a1][i] = x
                else:
                    if self.lazydata[a1]!=None:
                        self.data[a1][i] = self.lazydata[a1]
                s1 = self.func(s1,self.data[a1][i])
            self.func_num[a1] = s1
            self.lazydata[a1] = None
            for i in range(a1+1, a2):
                self.lazydata[i] = x
                self.func_num[i] = x
            s2 = self.ide
            for i in range(bucket_size):
                if i<b2:
                    self.data[a2][i] = x
                else:
                    if self.lazydata[a1]!=None:
                        self.data[a2][i] = self.lazydata[a2]
                s2 = self.func(s2,self.data[a2][i])
            self.lazydata[a2] = None
            self.func_num[a2] = s2
    
    def get(self, i):
        """0-indexedのi番目を取得で計算"""
        a, b = i//bucket_size, i%bucket_size
        if self.lazydata[a] != None:
            return self.lazydata[a]
        else:
            return self.data[a][b]
    
    def query(self,l,r):
        a1, b1 = l//bucket_size, l%bucket_size
        a2, b2 = r//bucket_size, r%bucket_size
        if a1==a2:
            if self.lazydata[a1]!=None:
                return self.lazydata[a1]
            else:
                res = self.ide
                for i in range(b1,b2):
                    res = self.func(res,self.data[a1][i])
                return res
        else:
            res = self.ide
            if self.lazydata[a1]!=None:
                res = self.lazydata[a1]
            else:
                for i in range(b1,bucket_size):
                    res = self.func(res, self.data[a1][i])
            for i in range(a1+1,a2):
                res = self.func(res, self.func_num[i])
            if self.lazydata[a2]!=None:
                res = self.func(res,self.lazydata[a2])
            else:
                for i in range(b2):
                    res = self.func(res, self.data[a2][i])
            return res
