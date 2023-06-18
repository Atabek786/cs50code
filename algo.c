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
    // base case
    if(n == 1)
        return 0;
    // even numbers
    else if((n % 2) == 0)
        return 1 + collatz(n/2);
    // odd numbers
    else
    return 1 + collatz(3*n + 1);

}