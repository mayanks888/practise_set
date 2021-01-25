#include <iostream>
using namespace std;

class Complex
{
    int a, b;
    double k,t;

public:
    Complex(){
        a = 0;
        b =0;
    }

    Complex(int x, int y)
    {
        a = x;
        b = y;
    }

    Complex(double z,double r)
    {
        k = z;
        t = r;
    }

    Complex(int x){
        a = x;
        b = 0;
    }

  

    void printNumber()
    {
        cout << "Your number is " << a << " + " << b << "i" << endl;
        cout << "Your number is " << k << " + " << t << "i" << endl;
    }
};
int main()
{
    Complex c1(4, 6);
    c1.printNumber();

    Complex c2(5);
    c2.printNumber();

    Complex c3;
    c3.printNumber();


    Complex c7(4.6, 6.7);
    c1.printNumber();
    return 0;
}
