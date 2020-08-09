#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    
    int total = 0;
    for (int i = 1; i < 6; i++)
    {
        int digit = n % 10;
        //printf ("%d\n", digit);
        total += digit;
        n /= 10;
    }
    printf ("%d\n", total);

    return 0;
}



