#include <cs50.h>
#include <stdio.h>

long long factorial(long long number);

int main ()
{
long long n = get_long_long ("Type a number: ");

if (factorial(long long number) > 9223372036854775807)
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