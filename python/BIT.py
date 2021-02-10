import random


class BIT:
    def __init__(self, n: int, v: int = 0):
        self.n = n
        self.l = [v for i in range(n+1)]

    def __len__(self) -> int:
        return self.n

    @classmethod
    def lsb(cls, i) -> int:
        return i & (-i)

    def update(self, i: int, j: int):
        return self.add(i, j-self.l[i])

    def add(self, i: int, j: int):
        k = j
        e = i
        while e < self.n+1:  # 1-indexed
            self.l[e] += k
            e += BIT.lsb(e)

    def sum(self, right: int, left: int = None) -> int:
        if left:
            return self.sum(left)-self.sum(right-1)
        self.raiseIndexError(right)
        ans = 0
        while right:
            ans += self.l[right]
            right -= BIT.lsb(right)
        return ans

    def __iter__(self):
        for i in self.l:
            yield i

    def __str__(self):
        return str(list(self))

    def __setitem__(self, key, value):
        self.raiseIndexError(key)
        self.update(key, value)

    def __getitem__(self, key):
        self.raiseIndexError(key)
        return self.l[key]

    def isIndexError(self, key):
        return key > self.n+1

    def raiseIndexError(self, key):
        if self.isIndexError(key):
            raise IndexError('list index out of range')


def checkBIT():
    b = BIT(10)
    print(b)
    for i in range(int(input())):
        u, t, f = map(int, input().split())
        if u == 1:
            b[t] = f
        else:
            print(b.sum(t, f))
    print(b, b[2])
    print(b.isIndexError(100))


def main():
    n = int(input())
    b = BIT(n)
    l = list(map(int, input().split()))
    ans = -n
    for i in l:
        b.add(i, 1)
        ans += b.sum(i, n)
    print(ans)


if __name__ == '__main__':
    main()
