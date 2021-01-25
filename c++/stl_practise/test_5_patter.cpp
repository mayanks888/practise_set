#include <iostream>
#include <bits/stdc++.h>

using namespace std;

// int main()
// {

//     for (int a = 0; a < 20; a++)
//     {
//          cout << " ";
//         for (int b = 20-1; b >a; b--)
//         {
//             for (int l=0;l<b;l++)
//             {
//             // cout << " "<<endl;
//             cout << "*";
//             }
//         }
//         cout<<endl;
//     }
// }
// ###############################3
// first 10 odd number sum

int main()
{
    // int counter = 0;
    // int valIncrement = 0;
    // int sumTotal = 0;
    int counter = 0, valIncrement = 0, sumTotal = 0;
    while (counter < 10)
    {
        valIncrement++;
        if (valIncrement % 2 != 0)
        {
            sumTotal = sumTotal + valIncrement;
            counter++;
        }
    }
    cout << "output of 10 odd number is " << sumTotal << endl;

    cout << "powe of counter is " << pow(sumTotal, 2);
}