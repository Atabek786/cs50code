#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int convert(string input);

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
    printf("%i\n", convert(input));
}

int convert(string input)
{
    // TODO
    int result = (atoi(input));
    int num = 0;
    int i = 0, sign = 1;

    while (input == ' ' || input == '\n' || input == '\t')
    {
        i++;
    }
    if (input == '+' || input == '-')
    {
        if(input == '-')
        {
            sign = -1;
        }
        i++;
    }

    while (input && (input >= '0' && input <= '9'))
    {
        num = num * 10 + (input - '0');
        i++;
    }
    return sign * num;
}