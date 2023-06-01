#include <stdio.h>
#include <cs50.h>

int main (void)
{
    // Get size of grid
    int n;
    do
    {
        n=get_int("Size: ");
    }
    while (n<1);

    //Print grid of bri ks
    for (int r=0 ; r<n; r++)
    {
        for (int c=0; c<n; c++)
        {
            printf("#");
        }
        printf("\n");
    }
}