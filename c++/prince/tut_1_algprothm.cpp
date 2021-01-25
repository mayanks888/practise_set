#include<iostream>
#include<algorithm>
using namespace std;

int main(){
int a[]={1,5,8,13,8,8,5,5,8,5,44};
sort(a, a+11);
int size=sizeof(a)/sizeof(*a);
for (int loop=0; loop<=size-1;loop++)
// for (int loop=0; loop<=11;loop++)
{
    cout<<a[loop]<<endl;
}
return 0;
}
