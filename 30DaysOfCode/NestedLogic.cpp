#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int d1, m1, y1;
    int d2, m2, y2;

    cin >> d2 >> m2 >> y2;
    cin >> d1 >> m1 >> y1;

    int fine = 0;

    if ((d2 <= d1 && m2 <= m1 && y2 <= y1) || (y2 < y1))
        fine = 0;
    else if (d2 > d1 && m2 <= m1 && y2 <= y1)
        fine = 15 * (d2 - d1);
    else if (m2 > m1 && y2 <= y1)
        fine = 500 * (m2 - m1);
    else
        fine = 10000;

    cout << fine << endl;

    return 0;
}



