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
    do
    {
        if (n == 1)
            return 1;
        else if (n % 2 == 0)
        return n/2;
        else
        return 3 * n + 1;
    }
    while (n > 0);

}