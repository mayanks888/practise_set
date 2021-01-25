#include<iostream>
#include<vector>

using namespace std;

void display_vec(vector<int>&ve)//&ve is a object of the vector not a variable concepts here.
{
//   for (int loop =0; loop<=ve.size();loop++)
// //   for (int loop =ve.begin(); loop<=ve.end();loop++)
//     {
//         cout<<"the values in vector are "<<ve.at(loop)<<endl;
//     }

    for (std::vector<int>::iterator it = ve.begin() ; it != ve.end(); ++it)
    std::cout << ' ' << *it;
    
}

int main(){
    vector<int>vec;
    vec.push_back(4);
    for (int loop =0;loop<=5;loop++)
    {
        vec.push_back(loop);
    }
    display_vec(vec);
    cout<<endl;
//first we have to create iterator which is nother but the pointer to the vector
//ite will point to fisrt element of the vector
vector <int> ::iterator ite =vec.begin();
// auto ite =vec.begin();//or you can directly ise use it will solve everything
cout<<"iteris is"<<*ite<<endl;

//insert fucntion is used to insert the value inwhere in the function
// vec.insert(ite+2, 787);
vec.insert(ite+2,4,78);
// display_vec(vec);
vec.swap(vec);
display_vec(vec);

cout<<endl;
// defining vector with values and size
vector <int> vec2 (2,16);
display_vec(vec2);
// cout<< <<endl;
return 0;
}