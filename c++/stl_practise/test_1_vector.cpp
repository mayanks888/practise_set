#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// int main()
// {
// vector<int >vec {1,2,3,4};
// vec.push_back(55);
// cout<<"mayank";
// // cout<vec[0]<<std::endl;

// }
// sort the vector

void display(vector<int> &vec2)
{
    vector<int>::iterator it;
    for (it = vec2.begin(); it != vec2.end(); it++)
        cout << *it << " ";
    cout << endl;
}

void display_2(vector<int> &vec)
{

    for (auto i : vec)
    {
        cout << i << " ";
    }
    cout << '\n';

}

int main()
{
    vector<int> vec{1, 6, 10, 8, 4, 2, 98};
    sort(vec.begin(), vec.end());

    display(vec);
    // #remove  value from vector
    auto new_end(remove(begin(vec), end(vec), 2));
    vec.erase(new_end, end(vec));
    // display(vec);
    display_2(vec);

    // auto new_end_2=remove_if(begin(vec), end(vec), odd);
    vec.erase(remove_if(begin(vec), end(vec), odd), end(vec));
    return 0;
}