# 参照　https://qiita.com/R_olldIce/items/32cbf5bc3ffb2f84a898#25-%E5%8F%96%E5%BE%97%E3%82%AF%E3%82%A8%E3%83%AA

# fの関数定義例
# f = lambda a, b: a+b  a*b  a ^ b
# gcdの時はUnitXは0で
# indexも欲しかったら以下みたいに
def op(a,b):
    if a[0]<b[0]:
        return a
    elif a[0]>b[0]:
        return b
    else:
        return (a[0],min(a[1],b[1]))

# 区間取得を行うときに最大をとる場合、以下参考
# https://yukicoder.me/submissions/766644
class SegmentTree():
    """UnitXは単位元、fは区間で行いたい操作、initは自然数あるいは配列"""
    def __init__(self, init, unitX, f):
        self.f = f # (X, X) -> X
        self.unitX = unitX
        self.f = f
        if type(init) == int:
            self.n = init
            self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * (self.n * 2)
        else:
            self.n = len(init)
            self.n = 1 << (self.n - 1).bit_length()
            # len(init)が2の累乗ではない時UnitXで埋める
            self.X = [unitX] * self.n + init + [unitX] * (self.n - len(init))
            # 配列のindex1まで埋める
            for i in range(self.n-1, 0, -1):
                self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
    
    def update(self, i, x):
        """0-indexedのi番目の値をxで置換"""
        # 最下段に移動
        i += self.n
        self.X[i] = x
        # 上向に更新
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
            i >>= 1
    
    def getvalue(self, i):
        """元の配列のindexの値を見る"""
        return self.X[i + self.n]
    
    def getrange(self, l, r):
        """区間[l, r)でのfを行った値"""
        l += self.n
        r += self.n
        al = self.unitX
        ar = self.unitX
        while l < r:
            # 左端が右子ノードであれば
            if l & 1:
                al = self.f(al, self.X[l])
                l += 1
            # 右端が右子ノードであれば
            if r & 1:
                r -= 1
                ar = self.f(self.X[r], ar)
            l >>= 1
            r >>= 1
        return self.f(al, ar)
    
    # Find r s.t. calc(l, ..., r-1) = True and calc(l, ..., r) = False
    def max_right(self, l, z):
        if l >= self.n: return self.n
        l += self.n
        s = self.unitX
        while 1:
            while l % 2 == 0:
                l >>= 1
            if not z(self.f(s, self.X[l])):
                while l < self.n:
                    l *= 2
                    if z(self.f(s, self.X[l])):
                        s = self.f(s, self.X[l])
                        l += 1
                return l - self.n
            s = self.f(s, self.X[l])
            l += 1
            if l & -l == l: break
        return self.n
    
    # Find l s.t. calc(l, ..., r-1) = True and calc(l-1, ..., r-1) = False
    def min_left(self, r, z):
        if r <= 0: return 0
        r += self.n
        s = self.unitX
        while 1:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not z(self.f(self.X[r], s)):
                while r < self.n:
                    r = r * 2 + 1
                    if z(self.f(self.X[r], s)):
                        s = self.f(self.X[r], s)
                        r -= 1
                return r + 1 - self.n
            s = self.f(self.X[r], s)
            if r & -r == r: break
        return 0
    
    def debug(self):
        print("debug")
        print([self.getvalue(i) for i in range(min(self.n, 20))])
    
N, Q = map(int, input().split())
A = [int(a) for a in input().split()]
st = SegmentTree([(n, i) for i, n in enumerate(A)], 0, max)
for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        st.update(a-1, b)
    elif t == 2:
        print(st.getrange(a-1, b))
    else:
        z = lambda x: x < b
        print(min(N, st.max_right(a-1, z)) + 1)


