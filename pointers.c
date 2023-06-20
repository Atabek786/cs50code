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

    printf("a has the value %i, located at %p\n", a, &a); //14
    printf("b has the value %i, located at %p\n", b, &b); //25
    printf("c has the value %i, located at %p\n", c, &c); //0x123 

}