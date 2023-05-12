class RollingHash:
    def __init__(self, S) -> None:
        """文字列->整数変換とhash生成"""
        self.mod = 1<<61-1
        self.base = 10**9+7
        S = [ord(i)-96 for i in S]
        self.pow = [1]*(len(S)+1)
        self.hash = [0]*(len(S)+1)
        for i in range(len(S)):
            self.pow[i+1] = (self.pow[i]*self.base)%self.mod
            self.hash[i+1] = (self.hash[i]*self.base+S[i])%self.mod
    def gethash(self, l, r) -> int:
        """区間[l,r)でのハッシュ値の取得"""
        return (self.hash[r]-self.hash[l]*self.pow[r-l])%self.mod

class RollingHash2:
    def __init__(self, S) -> None:
        """文字列->整数変換と2つの基数でのhash生成"""
        S = [ord(i)-96 for i in S]
        l = len(S)
        # self.base1 = 10**9+7
        # self.base2 = 10**5+7
        self.base1 = 10**5+7
        self.base2 = 10**3+7
        self.mod = (1<<61)-1
        self.pow1 = [1]*(l+1)
        self.pow2 = [1]*(l+1)
        self.hash1 = [0]*(l+1)
        self.hash2 = [0]*(l+1)
        for i in range(l):
            self.pow1[i+1] = (self.pow1[i]*self.base1)%self.mod
            self.pow2[i+1] = (self.pow2[i]*self.base2)%self.mod
            self.hash1[i+1] = (self.hash1[i]*self.base1+S[i])%self.mod
            self.hash2[i+1] = (self.hash2[i]*self.base2+S[i])%self.mod
    def gethash(self,l,r):
        """2つの基数でのハッシュ値を返す"""
        a = (self.hash1[r]-self.hash1[l]*self.pow1[r-l])%self.mod
        b = (self.hash2[r]-self.hash2[l]*self.pow2[r-l])%self.mod
        return a, b
    
    def is_same(self, l1, r1, l2, r2):
        """2つの区間[l1,r1)と[l2,r2)の２つの基数でのハッシュ値が一致すればok"""
        a1, b1 = self.gethash(l1, r1)
        a2, b2 = self.gethash(l2, r2)
        if (a1==a2) and (b1==b2):
            return True
        else:
            return False


