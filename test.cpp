#include <iostream>
using namespace std;

struct Base
{
    virtual void f() {cout<<"base"<<endl;}
};

struct Sub: Base
{
    virtual void f() {cout<<"sub"<<endl;}
};

int main()
{
    Base *p = new Sub();
    p->f();
}
