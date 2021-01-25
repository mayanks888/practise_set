#include <iostream>
using namespace std;

int main()
{
    const int k = 40;
    const int *p;
    p = &k;
    // *p=35;??you cannot chage the const value even with help of pointer is not possible

    cout << *p << endl;
}