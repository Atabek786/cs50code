#include <stdio.h>
#include <cs50.h>

int main (void)
{
    int n = get_int ("Size: ");
    for (int r=0 ; r<n; r++)
    {
        for (int c=0; c<n; c++)
        {
            printf("#");
        }
        printf("\n");
    }
}