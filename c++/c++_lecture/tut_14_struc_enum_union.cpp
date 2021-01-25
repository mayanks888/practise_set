#include<iostream>
#include<string>
using namespace std;

// this is how yo define struct
struct employee
{
int id;
string name;
string loc;
};


// this is how use type def
typedef struct people
{
int id;
string name;
string loc;
}peo;


// **************union*****************************
union moneypaid
{
int dollor;
int rupee;
int yen;    /* data */
};



int main(){
struct employee e1;
e1.id=545;
e1.name="Mayank";
e1.loc="mars";
cout <<e1.loc<<endl;
    
// **********************************
peo p2;
p2.id=121;
cout<<"typedef id is "<<p2.id<<endl;
// cout<< <<endl;

// ***************************************
union moneypaid mp;
mp.rupee=100;
cout <<mp.rupee<<endl;
mp.dollor=80;
cout <<mp.rupee<<endl;

cout <<mp.dollor<<endl;
// *******************enum**************************
// enum color{red , green ,yellow, black};
enum color{red=0 , green=1 ,yellow=3, black=4};//same thing
cout<<red<<endl;

return 0;
}