#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height, row, cols, space ;
    do
    {
        height = get_int ("Height: ");
    }
    while (height < 1 || height > 8) ;

    for (row = 0; row < height; row++)
    {
        printf ("#");
    }
    printf ("\n");

}