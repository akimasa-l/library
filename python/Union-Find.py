import sys
sys.setrecursionlimit(2*10**5)#必要に応じて

class UnionFind:#再帰上限に引っかかることがあるので
    def __init__(self,n):
        self.l=list(range(n))
        self.n=n
        self.rank=[0 for i in range(n)]
    def find(self,x):
        if self.l[x]==x:
            return x
        self.l[x]=self.find(self.l[x])
        return self.l[x]
    def union(self,x,y):
        if x==y:return
        if self.rank[x]>self.rank[y]:
            return self.union(y,x)
        a,b=self.find(x),self.find(y)
        self.l[a]=b
        self.rank[a]=max(self.rank[b]+1,self.rank[a])
    def isSame(self,x,y):
        return self.find(x)==self.find(y)
