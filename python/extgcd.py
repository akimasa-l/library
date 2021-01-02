gcd=lambda a,b:gcd(b%a,a)if a!=0 else b
def extgcd(a,b):#a*lx+b*ly=gcd(a,b)となる(lx,ly)を求める
    x,y,lx,ly=0,1,1,0
    while b>0:
        q=a//b
        a,b=b,a%b
        x,y,lx,ly=lx-q*x,ly-q*y,x,y
    return (lx,ly)
mod=10**9+7
modinv=lambda x:extgcd(x,mod)[0]
def ncr(n,r):
    k=1
    for i in range(n-r+1,n+1):
        k=i*k%mod
    for i in range(1,r+1):
        k=modinv(i)*k%mod
    return k