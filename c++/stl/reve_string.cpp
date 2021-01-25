// #include <iostream>
// #include <string>
// #include <algorithm>
// using namespace std;
 
// // Function to reverse a string in-place in C++
// void reverse(string &s)
// {
//     int n = s.length();
//     for (int i = 0; i < n/2; i++)
//         std::swap(s[i], s[n-i-1]);
// }
 
// int main()
// {
//     std::string s("Reverse a string in C++");
 
//     reverse(s);
//     cout << s;
 
//     return 0;
// }

#include <algorithm>  
#include <iostream>  
#include <string>  
  
using namespace std;  
  
int main() {  
  string str = "Hello Myself Nikita";  
  cout << "Before Reverse : "<< str << endl;  
  
  reverse(str.begin(), str.end());  
  cout <<"After Reverse  : " << str << endl;  
    
  return 0;  
}  