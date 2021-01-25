#include<iostream>
#include<vector>
#include<string>


using namespace std;

template<class T>
void display(vector<T>val)
{
    vector<int>::iterator it;

    for(it=val.begin();it!=val.end();it++)
    {
    cout<< *it<<" ";
    }
    cout<< endl;
}
template<class T>

void display_r(vector<T>vec)
{
    // vector<T>::iterator vec1_rIter;

    for( auto vec1_rIter = vec.rbegin(); vec1_rIter != vec.rend(); vec1_rIter++)

    cout<<*vec1_rIter<<' ';

    // for(it=val.rbegin();it!=val.rend();it++)
    // {
    // cout<< *it<<" ";
    // }
    cout<< endl;
}
int main()
{

vector <int > vec;

for (auto k=10;k<20;k++)
{
    vec.push_back(k);


}
display(vec);
display_r(vec);
cout<<vec.size()<<endl;
cout<<vec.capacity()<<endl;
cout<<vec.empty()<<endl;
vec.erase(vec.begin()+2);
// vec.clear();
cout<<*vec.begin();
cout<<vec.empty()<<endl;
vec.insert(vec.begin()+4,28);
vec.pop_back();
vec.resize(20,8);//it resize the vector to new




// vector <string> name {"God","is","Great"};
const string wrd="GOD is Great";
wrd.find("is");
std::size_t found = wrd.find("is");
// char *token = strtok(wrd, " "); 
// vector <string> name;
// name.push_back("god");
// name.push_back("is");
// name.push_back("great");
// name.(" ");

// display(name);


}