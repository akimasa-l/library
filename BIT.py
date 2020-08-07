import random
class BIT:
    def __init__(self,n,v=0):
        self.n=n
        self.l=[v for i in range(n+1)]
    def __len__(self):
        return self.n
    def lsb(self,i):
        return i&(-i)
    def update(self,i,j):
        k=j-self.l[i]
        e=i
        while e<self.n+1:
            self.l[e]+=k
            e+=self.lsb(e)
        return 
    def sum(self,right,left=None):
        if left:
            return self.sum(left)-self.sum(right-1)
        ans=0
        while right:
            ans+=self.l[right]
            right-=self.lsb(right)
        return ans
    def __iter__(self):
        return iter(self.l)
    def __str__(self):
        return str(list(self))

def checkBIT():
    b=BIT(10)
    print(b)
    for i in range(int(input())):
        u,t,f=input().split()
        t,f=map(int,(t,f))
        if u=='u':
            b.update(t,f)
        else:
            print(b.sum(t,f))
    print(b)

def main():
    checkBIT()

main()