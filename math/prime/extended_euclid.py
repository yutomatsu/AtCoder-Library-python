# 拡張ユークリッド
def extgcd(s,t):
    """a*s+b*t=gcd(s,t)となるような(gcd(s,t),a,b)を計算する"""
    s, bs = 0, 1
    r, br = t,s
    while r:
        q = br//r
        br,r = r,br-q*r
        bs,s = s,bs-q*s
    return br,bs,(br-bs*s)//t if t else 0
