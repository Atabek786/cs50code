#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Ask user for name, age and phone number

    string name = get_string("What's your name? ");
    int age = get_int("What's your age? ");
    long number = get_long ("What's your phone number? ");

    printf ("Name is %s. Age is %i. Phone number is %li.", name, age, number );
}