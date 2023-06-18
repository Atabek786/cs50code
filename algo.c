#include <cs50.h>
#include <stdio.h>

int collatz(int n);

int main ()
{
    int n = get_int ("Write a number: ");
    
    printf("%i")
}

int collatz(int n)
{
    do
    {
        if (n == 1)
            return 1;
        else if (n % 2 == 0)
        return n/2
        else
        return 3 * n + 1;
    }
    while (n > 0)

}