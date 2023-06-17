#include <cs50.h>
#include <stdio.h>

int factorial(int number);

int main ()
{
int n = get_int ("Type a number: ");


printf("%i\n", factorial(n));
}

int factorial(int number)
{
    if (number == 1)
    {
        return 1;
    }

    return number * factorial(number - 1);

    if (number > 2,147,483,647)
    {
        printf("Too big number.\n");
    }
}