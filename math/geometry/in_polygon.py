def in_polygon(p, P):
    """
    p:判定する点
    P:多角形の点群(反時計)
    """
    cnt = 0
    l = len(P)
    x, y = p
    for i in range(l):
        x0, y0 = P[i]
        x1, y1 = P[(i+1)%l]
        if min(x0,x1)<=x<=max(x0,x1) and min(y0,y1)<=y<=max(y0,y1) and (y-y0)*(x1-x0)==(y1-y0)*(x-x0):
            # 境界線上
            return 1
        if y0>y1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        if y0<=y<y1 and (x0-x)*(y1-y0)>(y0-y)*(x1-x0):
            cnt += 1
    return 2 if cnt&1 else 0
