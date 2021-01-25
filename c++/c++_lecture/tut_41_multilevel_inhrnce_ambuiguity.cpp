
#include <iostream>
using namespace std;

// Syntax for inheriting in multiple inheritance
// class DerivedC: visibility-mode base1, visibility-mode base2
// {
//      Class body of class "DerivedC"
// };

class Base1{
protected:
    int base1int;

public:
    void set_base1int(int a)
    {
        base1int = a;
    }
    void greet()
    {
        cout<<"hey everyone this is base 1 calling"<<endl;
    }
};

class Base2{
protected:
    int base2int;

public:
    void set_base2int(int a)
    {
        base2int = a;
    }

     void greet()
    {
        cout<<"hey everyone this is base 1 calling"<<endl;
    }
};

class Base3{
protected:
    int base3int;

public:
    void set_base3int(int a)
    {
        base3int = a;
    }
};

class Derived : public Base1, public Base2, public Base3
{
    public: 
        void show(){
            cout << "The value of Base1 is " << base1int<<endl;
            cout << "The value of Base2 is " << base2int<<endl;
            cout << "The value of Base3 is " << base3int<<endl;
            cout << "The sum of these values is " << base1int + base2int + base3int << endl;
        }
         void greet()
         {
             //this is know as ambiiguas inheritacne where two funciton with same name exist in two classes and 
            //  compiler gets confused to which one to take it.
             Base1::greet();
            //  Base2::greet();
         }
};
/*
The inherited derived class will look something like this:
Data members:
    base1int --> protected
    base2int --> protected

Member functions:
    set_base1int() --> public
    set_base2int() --> public
    set_show() --> public
*/
int main()
{
    Derived harry;
    harry.set_base1int(25);
    harry.set_base2int(5);
    harry.set_base3int(15);
    harry.show();
    harry.greet();
    
    return 0;
}















/*
#include <iostream>

using namespace std;

class base
{
protected:
    int data1 = 30;
};

class derv1
{
protected:
    int data2 = 40;
};

class derv2 : public derv1 , public base
{
protected:
    
    int data3;

public:
    void show()
    {
        cout << "the value of data1 is " << data1 << endl;
        cout << "the value of data2 is " << data2 << endl;
        cout << "the value of data1 is " << data1 + data2 << std::endl;
    }
};

int main()
{
    derv2 d2;
    d2.show();
}
*/