#include <stdio.h>
#include <cs50.h>

int main (void)
{
    int n;
    do
    {
        n=get_int("Size: ");
    }
    while (n<1);

    for (int r=0 ; r<n; r++)
    {
        for (int c=0; c<n; c++)
        {
            printf("#");
        }
        printf("\n");
    }
}