# https://atcoder.jp/contests/practice2/tasks/practice2_g

class SCC:
    def __init__(self,n):
        self.n = n
        self.edges = []
 
    def add_edge(self,a,b):
        self.edges.append((a,b))
 
    def scc(self):
        n = self.n
        counter = [0]*(n+1)
        elist = [0]*len(self.edges)
        for x,y in self.edges:
            counter[x+1] += 1
        for x in range(n):
            counter[x+1] += counter[x]
        start = counter[:]
        for x,y in self.edges:
            elist[counter[x]] = y
            counter[x] += 1
 
        k = 0
        low = [0]*n
        num = [-1]*n
        pre = [None]*n
        visited = []
        q = []
        sccs = []
        for x in range(n):
            if num[x] < 0:
                q.append(x)
                q.append(x)
                while q:
                    x = q.pop()
                    if num[x] < 0:
                        low[x] = num[x] = k
                        k += 1
                        visited.append(x)
                        for i in range(start[x],start[x+1]):
                            y = elist[i]
                            if num[y] < 0:
                                q.append(y)
                                q.append(y)
                                pre[y] = x
                            else:
                                low[x] = min(low[x],num[y])
                    else:
                        if low[x] == num[x]:
                            scc = []
                            while 1:
                                y = visited.pop()
                                num[y] = n
                                scc.append(y)
                                if x == y:
                                    break
                            sccs.append(scc)
                        y = pre[x]
                        if y is not None:
                            low[y] = min(low[y],low[x])
        return sccs[::-1]

n, m = map(int, input().split())
scc = SCC(n)
for _ in range(m):
    a,b=map(int,input().split())
    scc.add_edge(a,b)
ans = scc.scc()
print(len(ans))
for i in ans:
    print(len(i),*i)
