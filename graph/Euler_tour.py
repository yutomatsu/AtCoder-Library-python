N = 5
Euler = []
inout = [[-1]*2 for _ in range(N)]
G = [list() for _ in range(N)]

# dfs
def dfs(v, p):
    """
    オイラーツアー
    下向きに通る時その頂点番号
    上向きに通る時その頂点番号*(-1)
    """
    inout[v][0] = len(Euler)
    Euler.append(v)
    for nex in G[v]:
        if nex==p:
            continue
        dfs(nex, v)
        inout[nex][1] = len(Euler)
        Euler.append(-nex)

def dfs2():
    # stack
    p = [-1]*N
    stack = [(0,1)]
    while stack:
        v,t = stack.pop()
        if t==0:
            inout[v][1] = len(Euler)
            Euler.append(-v)
        else:
            inout[v][0] = len(Euler)
            Euler.append(v)
            stack.append((v,0))
            for nex in G[v]:
                if p[v]==nex:continue
                p[nex] = v
                stack.append((nex,1))

"""debug"""
G = [[1,2],[0,3,4],[0],[1],[1]]
# dfs(0,-1)
dfs2()
inout[0][1] = len(Euler)
print(*Euler)
for a, b in inout:
    print(a, b)

"""
0 1 3 -3 4 -4 -1 2 -2
0 9
1 6
7 8
2 3
4 5
"""