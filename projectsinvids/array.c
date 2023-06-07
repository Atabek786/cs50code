#include <cs50.h>
#include <stdio.h>

int main (void)
{
    //Get the length from the user
    int n;
    do
    {
    n = get_int ("Size of array: ");
    }
    while (n < 1);

    //Declare our array
    int array[n];

    //Set the first value
    array[0] = 1;
    printf ("%i\n",array[0]);
    for (int i = 1; i < n; i++)
    {
        //Make the current elemet twice the previous
        array[i] = 2 * array[i - 1];
        printf ("%i\n", array[i]);
    }
}