#include <cs50.h>
#include <stdio.h>

int main (int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Error!");
        return 1;
    }


    string filename = argv[1];
    FILE *file = fopen(filename, "r");

    if (file == NULL)
    {
        printf("No file found.\n");
        return 1;
    }


    
}