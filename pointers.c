#include <stdio.h>
#include <cs50.h>

int main()
{
    int a = 28;
    int b = 50;
    int *c = &a;

    *c = 14;
    c = &b;
    *c = 25;
}