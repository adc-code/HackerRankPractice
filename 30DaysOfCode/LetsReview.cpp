#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;

        for (int e = 0; e < s.size(); e+=2)
            cout << s[e];

        cout << " ";

        for (int e = 1; e < s.size(); e+=2)
            cout << s[e];

        cout << endl;
    }

    return 0;
}


