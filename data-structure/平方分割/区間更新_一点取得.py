bucket_size = 350
class SqrtDecomposition:
    def __init__(self, N, init,ide):
        """
        平方分割して、各バケット内での値を計算
        """
        self.N = N
        self.data = []
        self.lazydata = []
        d = []
        if init==0:
            for i in range(bucket_size):
                self.data.append([ide]*bucket_size)
                self.lazydata.append(None)
        else:
            for i in range(self.N):
                if (i+1)%bucket_size==0:
                    d.append(init[i])
                    self.data.append(d)
                    self.lazydata.append(None)
                    d = []
                else:
                    d.append(init[i])
            if d:
                self.data.append(d+[ide]*(bucket_size-len(d)))
                self.lazydata.append(None)
    
    def update(self, l, r, x):
        """0-indexedの[l,r)にxで更新"""
        # 更新処理をかく
        a1, b1 = l//bucket_size, l%bucket_size
        a2, b2 = r//bucket_size, r%bucket_size
        if a1==a2:
            if self.lazydata[a1] != None:
                for i in range(bucket_size):
                    if b1<=i<b2:
                        self.data[a1][i] = x
                    else:
                        self.data[a1][i] = self.lazydata[a1]
                self.lazydata[a1] = None
            else:
                for i in range(b1,b2):
                    self.data[a1][i] = x
        else:
            if self.lazydata[a1] != None:
                for i in range(bucket_size):
                    if i>=b1:
                        self.data[a1][i] = x
                    else:
                        self.data[a1][i] = self.lazydata[a1]
                self.lazydata[a1] = None
            else:
                for i in range(b1,bucket_size):
                    self.data[a1][i] = x
            for i in range(a1+1, a2):
                self.lazydata[i] = x
            if self.lazydata[a2] != None:
                for i in range(bucket_size):
                    if i<b2:
                        self.data[a2][i] = x
                    else:
                        self.data[a2][i] = self.lazydata[a2]
                self.lazydata[a2] = None
            else:
                for i in range(b2):
                    self.data[a2][i] = x
    
    def get(self, i):
        """0-indexedのi番目を取得で計算"""
        a, b = i//bucket_size, i%bucket_size
        if self.lazydata[a] != None:
            return self.lazydata[a]
        else:
            return self.data[a][b]