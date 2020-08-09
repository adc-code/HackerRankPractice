#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char input [1000];
    scanf ("%s", input);
    //printf ("%s\n", input);

    int count [10];

    for (int i = 0; i < 10; i++)
        count[i] = 0;

    for (int i = 0; i < strlen(input); i++)
    {
        if (isdigit(input[i]))
        {
            int value = input[i] - '0';
            count[value] += 1;
        }
    }

    for (int i = 0; i < 10; i++)
        printf ("%d ", count[i]);

    return 0;
}



