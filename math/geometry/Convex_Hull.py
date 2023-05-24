# Graham's scan
N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]


def judge(p1,p2,p3):
    # 同一直線上に3点以上の点を許容する時は=を外す
    return (p1[0]-p2[0])*(p3[1]-p2[1])-(p3[0]-p2[0])*(p1[1]-p2[1])>=0

def convex_hull(N,P):
    P.sort(key = lambda x:(x[0],x[1]))
    ret = []
    # 下側の凸包
    for i in range(N):
        # 追加された点を凸包の構成点としたときに、凸包に含まれない点を削除していく
        while len(ret)>1:
            if judge(ret[-2],ret[-1],P[i]):
                ret.pop()
            else:
                break
        ret.append(P[i])
    # 上側の凸包
    size = len(ret)
    for i in range(N-2,-1,-1):
        while len(ret)>size:
            if judge(ret[-2],ret[-1],P[i]):
                ret.pop()
            else:
                break
        ret.append(P[i])
    return ret
    
print(convex_hull(N,P))
