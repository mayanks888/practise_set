#include<iostream>
#include<vector>
using namespace std;
int main()
{
    auto val =2;
    auto text={"one ", "two", "three"};//here i dont even define it as array or the variable
    for(auto data : text)
    {
        cout<< data<< endl;
    }


    // defining vector now
    vector<int> dat;
    dat.push_back(3);
    dat.push_back(35);
    dat.push_back(356);

    for (auto new_dat : dat)
    {

        cout<< new_dat<<endl;
    }

    string str_val="mayank";//here its unusual that we have to particularly define string instead of auto

    for (auto val : str_val)
    {

        cout<< val<<endl;
    }

        return 0;
}