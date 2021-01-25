#include<iostream>
#include<map>
#include<string>

using namespace std;

void display(map<char,int> &mp)
{
    for (auto iter=mp.begin();iter!=mp.end();iter++)
    {
    cout<<iter->first<<endl;
    }
}

int main(){

 map<string, int> name;

//  name.insert{"mayank",45};
//  namse.insert{"sandy",90;}    
 name["mayank"]=32;
 name["sandy"]=30;
// display(name);

 for (auto iter=name.begin();iter!=name.end();iter++)
    {
    cout<<iter->first<<" "<<(*iter).second<<endl;//two ways to run iteraot of maps
    }
// cout<< <<endl;
return 0;
}