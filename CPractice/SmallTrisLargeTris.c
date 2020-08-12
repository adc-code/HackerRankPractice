#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;
void sort_by_area(triangle* tr, int n) {
	/**
	* Sort an array a of the length n
	*/
    
    for (int i = 0; i < n-1; i++)
    {
        for (int j = 0; j < n-i-1; j++)  
        {
            float P = (tr[j].a + tr[j].b + tr[j].c) / 2.0;
            float area1 = sqrt (P * (P - tr[j].a) * (P - tr[j].b) * (P - tr[j].c));

            P = (tr[j+1].a + tr[j+1].b + tr[j+1].c) / 2.0;
            float area2 = sqrt (P * (P-tr[j+1].a) * (P-tr[j+1].b) * (P-tr[j+1].c));

            if (area1 > area2) {
                triangle tmp = tr[j];
                tr[j] = tr[j + 1];
                tr[j + 1] = tmp;
            }
        }
    }
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}



