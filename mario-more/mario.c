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
        for (space = 0; space < height - row - 1; space++)
        {
            printf(" ");
        }
        for (cols = 0; cols <= row; cols++)
        {
            printf ("#");
        }
        printf ("  ");
        for (cols = 0; cols <= row; cols++)
        {
            printf ("#");
        }
        printf ("\n");
    }

}