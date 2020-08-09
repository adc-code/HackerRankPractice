#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf ("%d", &n);

    int *arr = (int*) malloc (n * sizeof(int));

    int total = 0;
    for (int i = 0; i < n; i++)
    {
        scanf ("%d", &arr[i]);
        total += arr[i];
    }
    
    printf ("%d\n", total);

    return 0;
}


