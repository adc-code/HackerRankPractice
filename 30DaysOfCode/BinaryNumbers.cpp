#include <bits/stdc++.h>

using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int currR = 0;
    int maxR  = 0;

    while (true)
    {
        int d = n / 2;
        int r = n % 2;

        if (r == 1)
        {
            currR++;
            if (currR > maxR)
                maxR = currR;
        }
        else
        {
            currR = 0;
        }

        if (d == 0) break;

        n = d;
    }

    cout << maxR << endl;

    return 0;
}



