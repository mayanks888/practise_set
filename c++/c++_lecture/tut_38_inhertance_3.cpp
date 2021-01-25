#include <iostream>
using namespace std;

class Base
{
private:
    int data1;
    int data2;

public:
    void setData();
    int getData1();
    int getData2();
};

class derived: public Base{

    int data3;

public:
    void process();
    void display();
};

void Base::setData()
{
    data1 = 23;
    data2 = 87;
}

int Base::getData1()
{
    cout << "data1 is " << data1 << endl;
    return data1;
}
int Base::getData2()
{
    cout << "data2 is " << data2 << endl;
    return data2;
}

void derived::process()
{
    data3 = getData1() + getData2();
}

void derived::display()
{
    cout << "data3 is " << data3 << endl;
}
int main()
{

    // Base mydat;
    // mydat.setData();
    // mydat.getData1();
    // mydat.getData2();

    derived derData;
    derData.setData();
    // derData.getData1();
    // derData.getData2();
    derData.process();
    derData.display();

    // cout<< <<endl;
    return 0;
}