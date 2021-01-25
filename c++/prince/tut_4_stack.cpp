#include <iostream>
#include <stack>
#include <vector>

using namespace std;

void display(stack<int> sta)
{
    //     for (stack<int>::iterator)
    while (!sta.empty())
    {
        // stack is vertical so top and bottom
        cout << sta.top()<<endl;
        sta.pop();
    }
}
int main()
{

    stack<int> st;
    for (int loop = 0; loop < 5; loop++)
    {
        st.push(loop);
    }
    display(st);
    // cout<<st <<endl;
    return 0;
}