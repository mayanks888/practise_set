#include<iostream>
using namespace std;
//dynamic pointer create memory at run time.
// now if create memory at run time than we have to clear memory it also
int main(){
    int a=10;
    int * d=&a;//this is normal pointers
cout<<"the address of pointer is"  << d<<endl;
cout<<"the value of pointer is"  << *d<<endl;
// cout<<"the value of pointer is"  << this->d<<endl;

int *dp = new int(40);
cout<<"the value of dynamic pointer dp is "  << *dp<<endl;

int k[3]={1,2,3};
int *ap = new int[4];
ap[0]=4;
ap[1]=5;
*(ap+2)=6;//another way to define
cout<<"the value of dynamic pointer dp is "  << ap[1]<<endl;
delete[] ap,dp;
return 0;
}