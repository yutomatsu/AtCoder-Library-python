"""実装"""
# 更新処理の際に区間でたせたところはself.add_dataに格納
# 一点取得の際にそのデータに格納されてる値と、
# その値が含まれる区間に足された値を足したものを返す

bucket_size = 350
class SqrtDecomposition:
    def __init__(self, N, init,ide):
        """
        平方分割して、各バケット内での値を計算
        """
        self.N = N
        self.data = []
        self.add_data = []
        d = []
        if init==0:
            for i in range(bucket_size):
                self.data.append([ide]*bucket_size)
                self.add_data.append(0)
        else:
            for i in range(self.N):
                if (i+1)%bucket_size==0:
                    d.append(init[i])
                    self.data.append(d)
                    self.add_data.append(0)
                    d = []
                else:
                    d.append(init[i])
            if d:
                self.data.append(d+[ide]*(bucket_size-len(d)))
                self.add_data.append(0)
    
    def add(self, l, r, x):
        """0-indexedの[l,r)にxを加算"""
        a1, b1 = l//bucket_size, l%bucket_size
        a2, b2 = r//bucket_size, r%bucket_size
        if a1==a2:
            for i in range(b1,b2):
                self.data[a1][i] += x
        else:
            for i in range(b1, bucket_size):
                self.data[a1][i] += x
            for i in range(a1+1, a2):
                self.add_data[i] += x
            for i in range(b2):
                self.data[a2][i] += x
    
    def get(self, i):
        """0-indexedのi番目を取得で計算"""
        a, b = i//bucket_size, i%bucket_size
        return self.data[a][b]+self.add_data[a]