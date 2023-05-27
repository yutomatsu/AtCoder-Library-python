def MillerRabin(N):
    """N<=1<<64なら決定的に素数判定ができる O(|A|logN)"""
    if N==2:
        return True
    if N==1 or N%2==0:
        return False
    if N<4759123141:
        A = [2,7,61]
    else:
        A = [2,325,9375,28178,450775,9780504,1795265022]
    
    s,d = 0,N-1
    while d%2==0:
        d >>= 1
        s += 1
    for a in A:
        if N<=a:return True
        num = pow(a,d,N)
        if num!=1:
            for _ in range(s):
                if num==N-1:break
                num *= num
                num %= N
            else:
                return False
    return True
