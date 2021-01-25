#include<iostream>
using namespace std;

class BaseClass{
    public:
        int var_base=1;
        virtual void display(){
            cout<<"1 Dispalying Base class variable var_base "<<var_base<<endl;
        }
};

class DerivedClass : public BaseClass{
    public:
            int var_derived=2;
            void display(){
                cout<<"2 Dispalying Base class variable var_base "<<var_base<<endl;
                cout<<"2 Dispalying Derived class variable var_derived "<<var_derived<<endl;
            }
};



int main()
{

BaseClass *base_cls;
BaseClass obj_base_cls;
DerivedClass obj_dev_cls;

base_cls= &obj_dev_cls;
base_cls->var_base=45;
base_cls->display();


DerivedClass *dev_cls;

dev_cls= &obj_dev_cls;
dev_cls->var_derived=945;
dev_cls->display();

}
