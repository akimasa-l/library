def extGCD(a,b,x,y):
    if b==0:
        x=1
        y=0
        return a
    d=extGCD(b,a%b,y,x)
    y-=(a//b)*x
    return d
def extGCDD(a,b):
    while b!=0:
        b=0###################################
def mod107(a):
    x,y=1,1
    extGCD(a,10**9+7,x,y)
    return x
def main():
    mod=10**9+7
    x=mod107(25)
    print(x,(x*13)%mod,(x*26)%mod)
    x,y=0,0
    print(extGCD(111,30,x,y))
    print(x,y)
main()