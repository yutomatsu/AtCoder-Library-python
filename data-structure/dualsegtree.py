class DualSegmentTree:
    def __init__(self,n,segfunc,ide):
        self.segfunc = segfunc
        self.ide_ele = ide
        self.num = 1<<(n-1).bit_length()
        self.data = [ide]*2*self.num

    def update(self,l,r,x):
        """[l,r)に対してsegfunc(data[i],x)で更新"""
        l += self.num
        r += self.num
        while l < r:
            if l&1:
                self.data[l] = self.segfunc(self.data[l],x)
                l += 1
            if r & 1:
                self.data[r-1] = self.segfunc(self.data[r-1],x)
            l >>= 1
            r >>= 1

    def get(self,idx):
        """idxの値を取得"""
        idx += self.num
        res = self.ide_ele
        while idx:
            res = self.segfunc(res,self.data[idx])
            idx>>=1
        return res