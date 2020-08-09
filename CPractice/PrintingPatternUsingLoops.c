#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
  	
    for (int i = n; i >= 1; i--)
    {
        int len = 0;
        for (int j = n; j >= i; j--)
        {
            len ++;
            printf ("%d ", j);
        }
        for (int j = 0; j < 2 * (n - len); j++)
            printf ("%d ", i);
        for (int j = i+1; j <= n; j++)
            printf ("%d ", j);

        //printf ("    %d %d", n - len, i);
        printf ("\n");
    }
    for (int i = 2; i <= n; i++)
    {
        int len = 0;
        for (int j = n; j >= i; j--)
        {
            len ++;
            printf ("%d ", j);
        }
        for (int j = 0; j < 2 * (n - len); j++)
            printf ("%d ", i);
        for (int j = i+1; j <= n; j++)
            printf ("%d ", j);

        printf ("\n");
    }

    return 0;
}



