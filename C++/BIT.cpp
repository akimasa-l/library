#include<iostream>
#include<vector>
using namespace std;


template<class T> struct BIT{
T n;
private:
vector<T> l(n+1,0);
};