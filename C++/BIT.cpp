#include<iostream>
#include<vector>
using namespace std;


using ll=long long;

template<class T> struct BIT{
using VT=vector<T>;
T n;
VT l;
BIT(const T& num):n(num),l(n+1,0){}
BIT(const T& num,const T& init_l):n(num),l(n+1,init_l){}
T lsb(T i){return i&(-i);}
T add(T i, T j){//add j to l_i
T e=i;
while(e<n+1){
    l.at(e)+=j;
    e+=lsb(e);
}
return j;
}
T update(T i,T j){//update j to l_i
return add(i,j-l.at(i))+j;
}
ll sum(T le,T ri){
return sum(ri)-sum(le-1);
}
ll sum(T le){
    ll ans=0;
    while(le>0){
        ans+=l.at(le);
        le-=lsb(le);
    }
    return ans;
}
};
int main(){
    
}