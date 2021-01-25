#include <iostream>
using namespace std;

class base
{
    int id, salary;

public:
    base(int a, int b) : id(a), salary(b)
    {
        cout << "hello costructor" << endl;
    }
    //default constructor
    base()
    {
    }
    void setdata(int x, int y)
    {
        id = x;
        salary = y;
    }

    void show()
    {
        cout << "the value of id and salary are " << id << " " << salary << endl;
    }
};

int main()
{

    // base b1(2,500);
    // b1.show();
    // // introcing pointer object and class
    // base *bp =&b1;
    // (*bp).show();//dereferecing and then take the values
    // bp->show(); //another way in pointer

    // ***********************************
    base *ptr = new base;
    ptr->setdata(5, 8888);
    ptr->show();

    // *********************************
    // array of object pointer
    base *bp_tr = new base[3];
    // base *b = new base[3];
    base *b = bp_tr;
    // bp_tr++->setdata(5, 6);

    for (int loop = 0; loop < 3; loop++)
    {
        // cout<<loop;
        bp_tr->setdata(loop + 100, loop + 5666);
        bp_tr++;
    }

    for (int loop = 0; loop < 3; loop++)
    {

        b->show();
        b++;
    }
    return 0;
}

// by harry
// *********************************************************************
/*
#include<iostream>
using namespace std;

class ShopItem
{
    int id;
    float price;
    public:
        void setData(int a, float b){
            id = a;
            price = b;
        }
        void getData(void){
            cout<<"Code of this item is "<< id<<endl;
            cout<<"Price of this item is "<<price<<endl;
        }
};
        // 1 2 3
        //     ^
        //     |
        //     |
        //     ptr
        // ptrTemp
int main(){
    int size = 3;
    // int *ptr = &size;
    // int *ptr = new int [34];

    // 1. general store item
    // 2. veggies item
    // 3. hardware item
    ShopItem *ptr = new ShopItem [size];
    ShopItem *ptrTemp = ptr;
    int p, i;
    float q;
    for (i = 0; i < size; i++)
    {
        cout<<"Enter Id and price of item "<< i+1<<endl;
        cin>>p>>q;
        // (*ptr).setData(p, q);
        ptr->setData(p, q);
        ptr++; 
    }

    for (i = 0; i < size; i++)
    {
        cout<<"Item number: "<<i+1<<endl;
        ptrTemp->getData();
        ptrTemp++;
    }
    
    
    return 0;
}
*/