def smallest_prime_factors(n):
    """各数の最小素因数を求める"""
    spf = [i for i in range(n+1)]
    for i in range(2,n+1):
        if i*i>n:
            break
        if spf[i] == i:
            for j in range(i*i, n+1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def fac(x, spf):
    """xを素因数分解,素因数のみ欲しい場合はsetに"""
    ret = []
    while x!=1:
        ret.append(spf[x])
        x //= spf[x]
    ret.sort()
    return ret

def fac2(x, spf) -> dict:
    """辞書で返す"""
    ret = {}
    while x!=1:
        if spf[x] in ret:
            ret[spf[x]] += 1
        else:
            ret[spf[x]] = 1
        x //= spf[x]
    return ret

def divisor(x,spf):
    """xの約数を列挙して返す"""
    ret = fac2(x,spf)
    div = [1]
    for key in ret.keys():
        s = len(div)
        for i in range(s):
            nn = key
            for j in range(1,ret[key]+1):
                div.append(div[i]*nn)
                nn *= key
    return div
