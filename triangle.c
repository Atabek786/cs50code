#include <stdio.h>
#include <cs50.h>
#include <string.h>

bool valid_triangle (float x, float y, float z);

int main (void)
{
    float a;
    a = get_float("Give a number a: ");
    float b;
    b = get_float("Give a number b: ");
    float c;
    c = get_float("Give a number c: ");

    if (a <=0 || b <= 0 || c <=0)
    {
        printf ("FALSE\n");
        return 0;
    }
    if ((a + b <= c) || (a + c <= b) || (b + c <= a))
    {
        printf ("FALSE\n");
        return 0;
    }
    else if ((a + b > c) || (a + c > b) || (b + c > a))
    {
        printf ("TRUE\n");
        return 0;
    }


}


bool valid_triangle (float x, float y, float z)
{
    //check for all positive sides
    if (x <= 0 || y <= 0 || z <= 0)
    {
        return false;
    }
    //check that sum of any two sides greater than third
    if ((x + y <= z) || (x + z <= y) || (y + z <= x))
    {
        return false;
    }
//if we passed both tests , then true
return true;
}

