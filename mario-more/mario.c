#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string height
    do
    {
        height = get_string ("Height: "); 
    }
    while (height < 1 || height > 8) ;
}