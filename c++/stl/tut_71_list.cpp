#include <iostream>
#include <list>

using namespace std;

void display_lis(list<int> &ve) //&ve is a object of the list not a variable concepts here.
{

    for (std::list<int>::iterator it = ve.begin(); it != ve.end(); ++it)
        std::cout << ' ' << *it;
    cout << endl;
}

bool single_digit(const int &value)
{
    return (value < 10);
}

// a predicate implemented as a class:
struct is_odd
{
    bool operator()(const int &value)
     { return (value % 2) == 1; }
};

int main()
{
    list<int> lis;
    lis.push_back(4);
    for (int loop = 0; loop <= 5; loop++)
    {
        lis.push_back(loop);
    }
    display_lis(lis);
    cout << endl;
    //first we have to create iterator which is nother but the pointer to the list
    //ite will point to fisrt element of the list
    list<int>::iterator ite = lis.begin();
    //insert fucntion is used to insert the value inwhere in the function
    // lis.insert(ite+2, 787);
    lis.insert(ite, 4, 78);
    // display_lis(lis);

    display_lis(lis);
    lis.reverse();
    lis.remove(2);
    display_lis(lis);

    // defining list with values and size
    list<int> lis2(2, 16);
    display_lis(lis2);

    // // cout<< <<endl;

    // **********************************************************

    // a predicate implemented as a function:

    // int main ()
    // {
    int myints[] = {15, 36, 7, 17, 20, 39, 4, 1};
    std::list<int> mylist(myints, myints + 8); // 15 36 7 17 20 39 4 1

    mylist.remove_if(single_digit); // 15 36 17 20 39

    mylist.remove_if(is_odd()); // 36 20

    std::cout << "mylist contains:";
    for (std::list<int>::iterator it = mylist.begin(); it != mylist.end(); ++it)
        std::cout << ' ' << *it;
    std::cout << '\n';

    return 0;
    // }
    // return 0;
}