#include <iostream>
using namespace std;

/*
Case1:
class B: public A{
   // Order of execution of constructor -> first A() then B()
};

Case2:
class A: public B, public C{
    // Order of execution of constructor -> B() then C() and A()
};

Case3:
class A: public B, virtual public C{
    // Order of execution of constructor -> C() then B() and A()
};

*/


class Base1
{
    int data_bse;

public:
    Base1(int a)
    {
        cout <<"bse1 called"<<endl;
        data_bse = a;
    }
};

class Base2
{
    int data_base2;

public:
    Base2(int b)
    {
                cout <<"bse2 called"<<endl;

        data_base2 = b;
    }
};

class derived : public Base1,  public Base2
// class derived : public Base1, virtual public Base2
{
    int data_drv;

public:
//this is how pass argument to the base class;
    derived(int first, int second, int third) : Base1(first), Base2(second)
    {
    data_drv = third;
    }
    void show()
    {
        cout << "all values are " <<  data_drv << endl;
    }
};

int main()
{
    derived d1(1, 2, 3);
    d1.show();
        // cout<< <<endl;
        return 0;
}