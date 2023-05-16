# 参考
# https://smijake3.hatenablog.com/entry/2018/06/16/144548

class LiChaoTree:
    def __init__(self,x):
        """最小値(最大値)を求める頂点の数"""
        x = sorted(list(set(x)))
        self.inf = 10**19
        self.L = 1<<(len(x)-1).bit_length()
        self.data = [None]*(2*self.L)
        self.x_data = x+[self.inf]*(self.L-len(x))
        self.idx = {num:id for id,num in enumerate(x)}
    
    def f(self,line,x):
        """line=(a,b),a*x+bを返す"""
        a,b = line
        return a*x+b
    
    def judge(self,line1,line2,x):
        """座標がxの点でline1の方が大きければTrueをそうでないならFalseを返す"""
        return self.f(line1,x)>self.f(line2,x)

    def add_line(self,line):
        """ax+bの直線を追加する"""
        id = 1
        l,r = 0,self.L
        while 1:
            if self.data[id] is None:
                self.data[id] = line
                return 
            m = (l+r)//2
            line_d = self.data[id]
            lx,mx,rx = self.x_data[l],self.x_data[m],self.x_data[r-1]
            f_l = self.judge(line_d,line,lx)
            f_m = self.judge(line_d,line,mx)
            f_r = self.judge(line_d,line,rx)
            if f_l and f_r:
                self.data[id] = line
                return
            if not f_l and not f_r:
                return
            if (f_r and f_m) or (f_m and f_l):
                line,self.data[id] = self.data[id],line
            if f_l!=f_m:
                r = m
                id = 2*id
            else:
                l = m
                id = 2*id+1
    
    def query(self,x):
        """座標xにおける直線群の最小値を返す"""
        id = self.idx[x]+self.L
        ans = self.inf
        while id:
            if self.data[id]:
                ans = min(ans,self.f(self.data[id],x))
            id >>= 1
        return ans
