//NOT SOLVED
#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int convert(string input[]);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input[]));
}

int convert(string input[])
{
    // TODO
    int result = (atoi(input[]));
    int num = 0;
    int i = 0, sign = 1;

    while (input[i] == ' ' || input[i] == '\n' || input[i] == '\t')
    {
        i++;
    }
    if (input[i] == '+' || input[i] == '-')
    {
        if(input[i] == '-')
        {
            sign = -1;
        }
        i++;
    }

    while (input[i] && (input[i] >= '0' && input[i] <= '9'))
    {
        num = num * 10 + (input[i] - '0');
        i++;
    }
    return sign * num;
}