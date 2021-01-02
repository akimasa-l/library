#include<iostream>
using namespace std;
using ll=long long;
template<ll mod>
class modint{
    ll a;
    public:
    modint()=default;
    modint(const ll& x):a(x){}// constructor
    friend ostream& operator<<(ostream& os,const modint& x){//cout<<modint
        return os << x;
    }
    friend istream& operator>>(istream& is,const modint& x){//cin>>modint
        return is >> x;
    }
    static modint extgcd(const modint& p,const modint& q,modint& x,modint& y){
        if(q==0){
            return 0;
        }
    }
    bool operator==(const modint& x)const{
        return this->a==x.a;
    }
    bool operator!=(const modint& x)const{
        return this->a!=x;
    }
    bool operator<(const modint& x)const{
        return this->a<x.a;
    }
    bool operator>(const modint& x)const{
        return this->a>x.a;
    }
    bool operator>=(const modint& x)const{
        return this->a>=x.a;
    }
    bool operator<=(const modint& x)const{
        return this->a<=x.a;
    }
    modint operator+(const modint& x)const{
        return (this->a+x.a)%mod;
    }
    modint operator-(const modint& x)const{
        return (this->a-x.a+mod)%mod;
    }
    modint operator++(int){
        this->a++;
        return *this;
    }
    bool f(){
        cout << a << endl;
        return 1;
    }

};
int main(){
    modint<99> n(3);
    cout << n << endl;
}