#include <cs50.h>
#include <stdio.h>

long long factorial(long long number);

int main ()
{
int n = get_int ("Type a number: ");

if (n > long long)
{
    printf("Too big number.\n");
}

printf("%lli\n", factorial(n));
}

long long factorial(long long number)
{
    if (number == 1)
    {
        return 1;
    }

    return number * factorial(number - 1);
}