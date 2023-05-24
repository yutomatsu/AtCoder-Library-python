"""
ax+bで表される直線群に対して、直線の追加及び任意のxに対して,
最小値を求める。
追加する直線の傾きは単調増加(減少)
計算する最小値(最大値)の座標xが単調増加(減少)

最大値を取りたい時は、傾きと切片を負で入れて
getの返り値に-かける
"""

from collections import deque

class Convex_Hull_Trick:
    def __init__(self):
        self.deq = deque()
 
    def check(self, f1, f2, f3):
        return (f2[0] - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])
 
    def f(self, f1, x):
        return f1[0] * x + f1[1]
 
    def add_line(self, a, b):
        """add f_i(x) = a*x + b"""
        f1 = (a, b)
        while len(self.deq) >= 2 and self.check(self.deq[-2], self.deq[-1], f1):
            self.deq.pop()
        self.deq.append(f1)
 
    def get(self, x):
        """min f_i(x)"""
        while len(self.deq) >= 2 and self.f(self.deq[0], x) >= self.f(self.deq[1], x):
            self.deq.popleft()
        return self.f(self.deq[0], x)
