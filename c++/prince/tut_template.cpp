#include <iostream>
using namespace std;

template <typename temp>

//template is used when we want to pass data tppes aa  a arguments so that
// we dont have to write a seprate function for differenet datatype for the same fucntion
temp add(temp a, temp b)
{
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
    // a=add(5.6,2.5);
    a = add<float>(5.6, 2.5);
    cout << a << endl;
    cout << add(5.6, 2.5) << endl;
    // cout<< <<endl;

    emp<double> e1; //define template here
    e1.get_salary(2.6646, 3.015) ;
    e1.showsalry();
    return 0;
}