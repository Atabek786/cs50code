#include <stdio.h>

int main (void)
{
    const int n=5;
    for (int r=0 ; r<n; r++)
    {
        for (int c=0; c<n; c++)
        {
            printf("#");
        }
        printf("\n");
    }
}