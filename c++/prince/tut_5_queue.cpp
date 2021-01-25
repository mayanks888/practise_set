#include <iostream>
#include <queue>
#include <vector>

using namespace std;

void display(queue<int> sta)
{
    //     for (queue<int>::iterator)
    while (!sta.empty())
    {
        //que is horizontal so its front 
        cout << sta.front()<<endl;
        sta.pop();
    }
}
int main()
{

    queue<int> qu;
    for (int loop = 0; loop < 5; loop++)
    {
        qu.push(loop);
    }
    display(qu);
    // cout<<st <<endl;
    return 0;
}