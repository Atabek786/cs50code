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
    while (end < start);

    // TODO: Calculate number of years until we reach threshold

    int years = 0;
    while (start <end)
    {
    start += start/12;
    years++;
    }

    // TODO: Print number of years

    
}
