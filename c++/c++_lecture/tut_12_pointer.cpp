#include<iostream>
using namespace std;

int main(){
    int a=3;
    int* b=&a;
    int k=*b;//this is defereing pointer
    cout<<"value if k "<< k <<endl;


    //try to work on the address of the pointer
    int** c = &b;//this adress of the pointer
cout<<b <<endl;
cout<<*b <<endl;
cout<<c <<endl;
cout<<*c <<endl;
return 0;
}