#include <cs50.h>
#include <stdio.h>

float average (int scores[]);

int main (void)
{
    int scores[3] ;
    for (int i = 0; i <3; i++)
{
    scores[i] = get_int ("Type your score: ");
}

    printf ("Your average score is %i \n", average (scores) );
}