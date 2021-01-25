#include <iostream>
using namespace std;

//template is used when we want to pass data tppes aa  a arguments so that
// we dont have to write a seprate function for differenet datatype for the same fucntion

// template <typename temp>
// or
template <class temp>
temp add(temp a, temp b)
{
    cout << "template one ran" << endl;

    return (a + b);
}

//template overloading function

int add(int a, int b)
{
    cout << "normal one ran" << endl;
    return (a + b);
}

template <class cl>

class emp
{
    cl id;
    cl salary;

public:
    void get_salary(cl a, cl b)
    {
        id = a;
        salary = b;
    }
    void showsalry()
    {
        cout << "id is " << id << " and salary is " << salary << endl;
    }
};

int main()
{
    int a;
    a=add(5,2);//when we give real datatypes values then the original fucntion run and not he template funtion.
    a = add<float>(5.6, 2.5);
    cout << a << endl;
    cout << add(5.6, 2.5) << endl;
    // cout<< <<endl;

    emp<double> e1; //define template here
    e1.get_salary(2.6646, 3.015);
    e1.showsalry();
    return 0;
}