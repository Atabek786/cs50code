#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size

    int start;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 0);

    // TODO: Prompt for end size

    int end;
    do
    {
        end = get_end("End size: ");
    }
    while (start < 0);

    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years
}
