#include <cs50.h>
#include <stdio.h>

int collatz(int n);

int main ()
{
    int number, result;
    number = get_int("Enter a number: ");

    result = collatz(number);

    printf("collatz = %i\n", result);
    return 0;
}

int collatz(int n)
{
    int product = 1;
    while(n > 0)
    {
        product *= n;
        n--;
    }
    return product;
}