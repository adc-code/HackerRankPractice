#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;


int main() {
    map <string, string>   phoneNums;

    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        string name, number;
        cin >> name >> number;
        map <string, string>::iterator it = phoneNums.find(name);
        if (it != phoneNums.end())
            phoneNums[name] = number;
        else
            phoneNums.insert(pair<string, string>(name, number));
    } 

    string name;
    while (cin >> name)
    {
        map <string, string>::iterator it = phoneNums.find(name);

        if (it != phoneNums.end())
            cout << name << "=" << it->second << endl;
        else
            cout << "Not found" << endl;
    }

    return 0;
}


