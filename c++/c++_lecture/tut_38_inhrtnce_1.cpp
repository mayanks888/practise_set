// #include <iostream>
// using namespace std;

// class employee
// {
//     // int salary;
//     // int id;

// public:
//     int salary;
//     int id;//for inheritance
//     employee();
//     employee(int a, int b)
//     {
//         salary = a;
//         id = b;
//     }
//     void show()
//     {
//         cout <<"the value of id is "<< id << " and the salary is "<< salary <<endl;
//     }
// };

// class emp : public employee
// {
//     // int languagecode;

// public:
    
//     emp(int c)
//     {
//         id = c;
//     }

//     void show()
//     {
//         cout <<"the value of id is "<<id<<endl;
//     }
// };

// int main();
// {
//     employee mayank(4,56666);
//     mayank.show();
//     emp langcode(9);
//     langcode.show();
//     // cout <<"hello" << endl;
//     return 0;
// }


#include <iostream>
using namespace std;

// Base Class
class Employee
{
public:
    int id;
    float salary;
    Employee(int inpId,float salinp)
    {
        id = inpId;
        salary = salinp;
    }
    Employee() {}
};

// Derived Class syntax
/*
class {{derived-class-name}} : {{visibility-mode}} {{base-class-name}}
{
    class members/methods/etc...
}
Note:
1. Default visibility mode is private
2. Public Visibility Mode: Public members of the base class becomes Public members of the derived class
3. Private Visibility Mode: Public members of the base class becomes Private members of the derived class
4. Private members are never inherited
*/

// Creating a Programmer class derived from Employee Base class
class Programmer : public Employee
{
public:
    int languageCode;
    Programmer(int inpId)
    {
        id = inpId;
        languageCode = 9;
    }
    void getData(){
        cout<<id<<endl;
    }
};

int main()
{
    Employee harry(1,5454), rohan(2,54545);
    cout << harry.salary << endl;
    cout << rohan.salary << endl;
    Programmer skillF(10);
    cout << skillF.languageCode<<endl;
    cout << skillF.id<<endl;
    skillF.getData();
    return 0;
}