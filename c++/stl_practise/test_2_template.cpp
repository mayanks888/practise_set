#include<iostream>
using namespace std;


template <class T>
T add(T a, T b)
{
return a+b;

}

template <class T>
T max_val(T a, T b)
{
return (a>b?a:b);

}
int main()
{
// cout<<add(2,6);
cout<<max_val(2,6);


}